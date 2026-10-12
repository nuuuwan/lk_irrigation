# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--12_17:38:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **286,035 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 17:38:57 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.134 |  |
| 2026-10-12 17:11:51 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 17:11:10 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-10-12 17:08:16 | Thawalama (Gin Ganga) | 2.38 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-10-12 17:07:49 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-10-12 17:07:42 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.056 |  |
| 2026-10-12 17:07:33 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-12 17:07:00 | Baddegama (Gin Ganga) | 2.56 | 🟢 Normal | -0.021 |  |
| 2026-10-12 17:05:55 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-10-12 17:05:49 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-10-12 17:05:28 | Badalgama (Maha Oya) | 3.25 | 🟢 Normal | -0.041 |  |
| 2026-10-12 17:05:27 | Magura (Kalu Ganga) | 2.33 | 🟢 Normal | -0.013 |  |
| 2026-10-12 17:05:03 | Ellagawa (Kalu Ganga) | 6.95 | 🟢 Normal | -0.058 |  |
| 2026-10-12 17:04:55 | Hanwella (Kelani Ganga) | 3.29 | 🟢 Normal | 0.000 |  |
| 2026-10-12 17:04:55 | Rathnapura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.039 |  |
| 2026-10-12 17:04:38 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-10-12 17:04:09 | Dunamale (Aththanagalu Oya) | 2.50 | 🟢 Normal | -0.047 |  |
| 2026-10-12 17:04:04 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.019 |  |
| 2026-10-12 17:03:54 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 17:03:14 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-12 17:03:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.96 | 🟢 Normal | -0.020 |  |
| 2026-10-12 17:03:06 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-10-12 17:03:05 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-10-12 17:02:49 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | -0.030 |  |
| 2026-10-12 17:02:44 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 17:02:27 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | -0.069 |  |
| 2026-10-12 17:02:19 | Panadugama (Nilwala Ganga) | 4.45 | 🟢 Normal | -0.039 |  |
| 2026-10-12 17:02:18 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-12 17:02:08 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-10-12 17:01:55 | Thalgahagoda (Nilwala Ganga) | 1.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-12 17:01:47 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-12 17:01:41 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | -0.018 |  |
| 2026-10-12 17:01:40 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-10-12 17:01:23 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 17:01:20 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-10-12 17:01:09 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-10-12 17:00:15 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-12 17:00:09 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 17:05:49 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-10-12 17:08:16 | Thawalama (Gin Ganga) | 2.38 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-10-12 17:04:38 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-10-12 17:07:49 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-10-12 17:11:10 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-10-12 17:07:33 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-12 17:01:55 | Thalgahagoda (Nilwala Ganga) | 1.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-12 17:00:09 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | 0.000 |  |
| 2026-10-12 17:00:15 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-12 17:11:51 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 17:01:23 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 17:02:44 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 17:01:47 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-12 17:04:55 | Hanwella (Kelani Ganga) | 3.29 | 🟢 Normal | 0.000 |  |
| 2026-10-12 17:03:54 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 17:02:18 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-12 17:05:55 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-10-12 17:01:09 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-10-12 17:02:08 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-10-12 17:03:14 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-12 17:03:06 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-10-12 16:03:28 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-10-12 17:01:20 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-10-12 17:05:27 | Magura (Kalu Ganga) | 2.33 | 🟢 Normal | -0.013 |  |
| 2026-10-12 17:01:41 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | -0.018 |  |
| 2026-10-12 17:04:04 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.019 |  |
| 2026-10-12 17:03:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.96 | 🟢 Normal | -0.020 |  |
| 2026-10-12 17:01:40 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-10-12 17:07:00 | Baddegama (Gin Ganga) | 2.56 | 🟢 Normal | -0.021 |  |
| 2026-10-12 17:03:05 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-10-12 17:02:49 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | -0.030 |  |
| 2026-10-12 17:02:19 | Panadugama (Nilwala Ganga) | 4.45 | 🟢 Normal | -0.039 |  |
| 2026-10-12 17:04:55 | Rathnapura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.039 |  |
| 2026-10-12 17:05:28 | Badalgama (Maha Oya) | 3.25 | 🟢 Normal | -0.041 |  |
| 2026-10-12 17:04:09 | Dunamale (Aththanagalu Oya) | 2.50 | 🟢 Normal | -0.047 |  |
| 2026-10-12 17:07:42 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.056 |  |
| 2026-10-12 17:05:03 | Ellagawa (Kalu Ganga) | 6.95 | 🟢 Normal | -0.058 |  |
| 2026-10-12 17:02:27 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | -0.069 |  |
| 2026-10-12 17:38:57 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.134 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)