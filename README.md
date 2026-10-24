# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--24_08:09:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **296,491 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 08:09:15 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-24 08:08:11 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -0.018 |  |
| 2026-10-24 08:07:21 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-24 08:06:57 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.022 |  |
| 2026-10-24 08:06:39 | Rathnapura (Kalu Ganga) | 2.39 | 🟢 Normal | -0.039 |  |
| 2026-10-24 08:06:15 | Galgamuwa (Mee Oya) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-10-24 08:06:06 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.009 |  |
| 2026-10-24 08:05:33 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-24 08:05:17 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | -0.070 |  |
| 2026-10-24 08:05:13 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | -0.020 |  |
| 2026-10-24 08:05:10 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | -0.069 |  |
| 2026-10-24 08:05:07 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | -0.019 |  |
| 2026-10-24 08:04:33 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-24 08:04:31 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-24 08:04:31 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-10-24 08:04:15 | Thalgahagoda (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-24 08:04:13 | Glencourse (Kelani Ganga) | 11.31 | 🟢 Normal | -0.080 |  |
| 2026-10-24 08:04:11 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | -0.024 |  |
| 2026-10-24 08:04:01 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-24 08:03:40 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-10-24 08:03:31 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-24 08:03:27 | Ellagawa (Kalu Ganga) | 6.48 | 🟢 Normal | -0.049 |  |
| 2026-10-24 08:03:13 | Hanwella (Kelani Ganga) | 3.61 | 🟢 Normal | -0.020 |  |
| 2026-10-24 08:03:08 | Peradeniya (Mahaweli Ganga) | 2.87 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-24 08:03:08 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-24 08:03:01 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 08:02:46 | Moragaswewa (Deduru Oya) | 3.33 | 🟢 Normal | -0.068 |  |
| 2026-10-24 08:02:30 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-10-24 08:02:22 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.030 |  |
| 2026-10-24 08:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.07 | 🟢 Normal | -0.030 |  |
| 2026-10-24 08:02:12 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-24 08:02:05 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-24 08:01:44 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-24 08:01:37 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-24 08:01:21 | Thanthirimale (Malwathu Oya) | 1.94 | 🟢 Normal | -0.022 |  |
| 2026-10-24 08:01:16 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.102 |  |
| 2026-10-24 08:01:13 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 08:01:10 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-24 08:00:56 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.091 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 08:07:21 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-24 08:01:44 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-24 08:03:08 | Peradeniya (Mahaweli Ganga) | 2.87 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-24 08:09:15 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-24 08:03:08 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-24 08:03:01 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 08:01:13 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 08:01:10 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-24 08:01:37 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-24 08:02:05 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-24 08:04:33 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-24 08:04:31 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-10-24 08:05:33 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-24 08:02:12 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-24 08:04:01 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-24 08:04:15 | Thalgahagoda (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-24 08:03:31 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-24 08:06:06 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.009 |  |
| 2026-10-24 08:02:30 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-10-24 08:06:15 | Galgamuwa (Mee Oya) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-10-24 08:08:11 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -0.018 |  |
| 2026-10-24 08:05:07 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | -0.019 |  |
| 2026-10-24 08:05:13 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | -0.020 |  |
| 2026-10-24 08:03:40 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-10-24 08:03:13 | Hanwella (Kelani Ganga) | 3.61 | 🟢 Normal | -0.020 |  |
| 2026-10-24 00:04:07 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.021 |  |
| 2026-10-24 08:01:21 | Thanthirimale (Malwathu Oya) | 1.94 | 🟢 Normal | -0.022 |  |
| 2026-10-24 08:06:57 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.022 |  |
| 2026-10-24 08:04:11 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | -0.024 |  |
| 2026-10-24 08:02:22 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.030 |  |
| 2026-10-24 08:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.07 | 🟢 Normal | -0.030 |  |
| 2026-10-24 08:06:39 | Rathnapura (Kalu Ganga) | 2.39 | 🟢 Normal | -0.039 |  |
| 2026-10-24 08:03:27 | Ellagawa (Kalu Ganga) | 6.48 | 🟢 Normal | -0.049 |  |
| 2026-10-24 08:02:46 | Moragaswewa (Deduru Oya) | 3.33 | 🟢 Normal | -0.068 |  |
| 2026-10-24 08:05:10 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | -0.069 |  |
| 2026-10-24 08:05:17 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | -0.070 |  |
| 2026-10-24 08:04:13 | Glencourse (Kelani Ganga) | 11.31 | 🟢 Normal | -0.080 |  |
| 2026-10-24 08:00:56 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.091 |  |
| 2026-10-24 08:01:16 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)