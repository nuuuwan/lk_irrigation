# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--22_09:16:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **322,571 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 09:16:01 | Panadugama (Nilwala Ganga) | 4.63 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:08:51 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.011 |  |
| 2026-11-22 09:08:16 | Galgamuwa (Mee Oya) | 0.48 | 🟢 Normal | -0.009 |  |
| 2026-11-22 09:07:57 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:07:55 | Panadugama (Nilwala Ganga) | 4.63 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:07:13 | Kuda Oya (Kirindi Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:06:49 | Rathnapura (Kalu Ganga) | 2.98 | 🟢 Normal | -0.057 |  |
| 2026-11-22 09:06:31 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.056 |  |
| 2026-11-22 09:05:09 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:05:09 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | -0.031 |  |
| 2026-11-22 09:04:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.83 | 🟢 Normal | -0.019 |  |
| 2026-11-22 09:04:23 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-11-22 09:04:04 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-22 09:03:54 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-11-22 09:03:51 | Ellagawa (Kalu Ganga) | 5.44 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-22 09:03:51 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.046 |  |
| 2026-11-22 09:03:46 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-11-22 09:03:34 | Urawa (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.012 |  |
| 2026-11-22 09:03:34 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-22 09:03:29 | Badalgama (Maha Oya) | 3.13 | 🟢 Normal | -0.020 |  |
| 2026-11-22 09:03:19 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:03:01 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-22 09:03:00 | Hanwella (Kelani Ganga) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-11-22 09:02:41 | Thanamalwila (Kirindi Oya) | 1.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 09:02:34 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-22 09:02:21 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-22 09:02:12 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.718 | 🔺 Rising |
| 2026-11-22 09:02:10 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:01:20 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:01:20 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-11-22 09:01:13 | Kuda Oya (Kirindi Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:01:07 | Moragaswewa (Deduru Oya) | 3.15 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:01:00 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.012 |  |
| 2026-11-22 09:00:59 | Weraganthota (Mahaweli Ganga) | -2.01 | 🟢 Normal | -1.119 |  |
| 2026-11-22 09:00:46 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 09:00:35 | Moraketiya (Walawe Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:00:17 | Pitabeddara (Nilwala Ganga) | 1.41 | 🟢 Normal | -0.040 |  |
| 2026-11-22 09:00:10 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-11-22 09:00:08 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-22 08:59:31 | Moragaswewa (Deduru Oya) | 3.15 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 09:02:12 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.718 | 🔺 Rising |
| 2026-11-22 09:03:01 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-22 09:03:51 | Ellagawa (Kalu Ganga) | 5.44 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-22 09:02:34 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-22 09:04:04 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-22 09:02:21 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-22 09:03:34 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-22 09:02:41 | Thanamalwila (Kirindi Oya) | 1.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 09:00:46 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 09:02:10 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:01:07 | Moragaswewa (Deduru Oya) | 3.15 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:01:20 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:03:19 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:16:01 | Panadugama (Nilwala Ganga) | 4.63 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:00:35 | Moraketiya (Walawe Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:00:08 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:07:57 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:05:09 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:07:13 | Kuda Oya (Kirindi Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-11-22 09:08:16 | Galgamuwa (Mee Oya) | 0.48 | 🟢 Normal | -0.009 |  |
| 2026-11-22 09:03:46 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-11-22 09:03:54 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-11-22 09:00:10 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-11-22 09:01:20 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-11-22 09:08:51 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.011 |  |
| 2026-11-22 09:01:00 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.012 |  |
| 2026-11-22 09:03:34 | Urawa (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.012 |  |
| 2026-11-22 09:04:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.83 | 🟢 Normal | -0.019 |  |
| 2026-11-22 09:04:23 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-11-22 09:03:29 | Badalgama (Maha Oya) | 3.13 | 🟢 Normal | -0.020 |  |
| 2026-11-22 09:03:00 | Hanwella (Kelani Ganga) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-11-22 09:05:09 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | -0.031 |  |
| 2026-11-22 09:00:17 | Pitabeddara (Nilwala Ganga) | 1.41 | 🟢 Normal | -0.040 |  |
| 2026-11-22 09:03:51 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.046 |  |
| 2026-11-22 09:06:31 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.056 |  |
| 2026-11-22 09:06:49 | Rathnapura (Kalu Ganga) | 2.98 | 🟢 Normal | -0.057 |  |
| 2026-11-22 09:00:59 | Weraganthota (Mahaweli Ganga) | -2.01 | 🟢 Normal | -1.119 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)