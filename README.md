# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--22_16:32:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **322,848 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 16:32:53 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-11-22 16:26:00 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-11-22 16:22:35 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-22 16:16:33 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | -0.009 |  |
| 2026-11-22 16:11:24 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.953 |  |
| 2026-11-22 16:10:17 | Peradeniya (Mahaweli Ganga) | 2.37 | 🟢 Normal | -0.009 |  |
| 2026-11-22 16:10:10 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | -0.048 |  |
| 2026-11-22 16:08:23 | Panadugama (Nilwala Ganga) | 4.46 | 🟢 Normal | -0.019 |  |
| 2026-11-22 16:06:59 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | -0.045 |  |
| 2026-11-22 16:06:30 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-22 16:05:43 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.057 |  |
| 2026-11-22 16:05:36 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-22 16:05:23 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-22 16:05:20 | Glencourse (Kelani Ganga) | 9.38 | 🟢 Normal | -0.058 |  |
| 2026-11-22 16:05:09 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.060 |  |
| 2026-11-22 16:05:06 | Moragaswewa (Deduru Oya) | 3.70 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-22 16:04:47 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-11-22 16:04:23 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-22 16:04:17 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 16:04:14 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-22 16:04:07 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.091 |  |
| 2026-11-22 16:04:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | -0.079 |  |
| 2026-11-22 16:03:20 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.011 |  |
| 2026-11-22 16:03:15 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-22 16:03:14 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | -0.030 |  |
| 2026-11-22 16:03:05 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | -0.010 |  |
| 2026-11-22 16:02:58 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 16:02:58 | Weraganthota (Mahaweli Ganga) | -2.45 | 🟢 Normal | -0.038 |  |
| 2026-11-22 16:02:14 | Horowpothana (Yan Oya) | 2.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 16:02:14 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-22 16:02:08 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-22 16:02:08 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | -0.041 |  |
| 2026-11-22 16:01:42 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-11-22 16:01:38 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 16:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-22 16:01:14 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-11-22 16:01:12 | Thanamalwila (Kirindi Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-11-22 16:01:08 | Moraketiya (Walawe Ganga) | 2.90 | 🟢 Normal | -0.021 |  |
| 2026-11-22 16:00:58 | Manampitiya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.052 |  |
| 2026-11-22 16:00:20 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 16:05:36 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-22 16:05:06 | Moragaswewa (Deduru Oya) | 3.70 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-22 16:03:15 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-22 16:04:23 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-22 16:06:30 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-22 16:02:08 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-22 16:02:58 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 16:02:14 | Horowpothana (Yan Oya) | 2.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 16:04:17 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 16:05:23 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-22 16:32:53 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-11-22 16:02:14 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-22 16:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-22 16:01:38 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 16:26:00 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-11-22 16:22:35 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-22 16:04:14 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-22 16:16:33 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | -0.009 |  |
| 2026-11-22 16:10:17 | Peradeniya (Mahaweli Ganga) | 2.37 | 🟢 Normal | -0.009 |  |
| 2026-11-22 16:01:14 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-11-22 16:01:42 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-11-22 16:03:05 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | -0.010 |  |
| 2026-11-22 16:00:20 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-11-22 16:01:12 | Thanamalwila (Kirindi Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-11-22 16:03:20 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.011 |  |
| 2026-11-22 16:08:23 | Panadugama (Nilwala Ganga) | 4.46 | 🟢 Normal | -0.019 |  |
| 2026-11-22 16:01:08 | Moraketiya (Walawe Ganga) | 2.90 | 🟢 Normal | -0.021 |  |
| 2026-11-22 16:03:14 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | -0.030 |  |
| 2026-11-22 16:02:58 | Weraganthota (Mahaweli Ganga) | -2.45 | 🟢 Normal | -0.038 |  |
| 2026-11-22 16:02:08 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | -0.041 |  |
| 2026-11-22 16:06:59 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | -0.045 |  |
| 2026-11-22 16:10:10 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | -0.048 |  |
| 2026-11-22 16:00:58 | Manampitiya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.052 |  |
| 2026-11-22 16:05:43 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.057 |  |
| 2026-11-22 16:05:20 | Glencourse (Kelani Ganga) | 9.38 | 🟢 Normal | -0.058 |  |
| 2026-11-22 16:05:09 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.060 |  |
| 2026-11-22 16:04:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | -0.079 |  |
| 2026-11-22 16:04:07 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.091 |  |
| 2026-11-22 16:11:24 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.953 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)