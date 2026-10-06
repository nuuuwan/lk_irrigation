# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--06_11:30:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **280,411 measurements** from **39** stations.
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
| 2026-10-06 11:30:07 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.024 |  |
| 2026-10-06 11:19:17 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-06 11:17:44 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-10-06 11:16:42 | Panadugama (Nilwala Ganga) | 3.78 | 🟢 Normal | -0.050 |  |
| 2026-10-06 11:10:53 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-06 11:10:16 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-10-06 11:09:05 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-06 11:07:35 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-06 11:07:02 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-10-06 11:05:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.87 | 🟢 Normal | -0.038 |  |
| 2026-10-06 11:05:50 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-06 11:05:43 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-06 11:05:17 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-10-06 11:05:00 | Glencourse (Kelani Ganga) | 11.48 | 🟢 Normal | -0.095 |  |
| 2026-10-06 11:04:37 | Badalgama (Maha Oya) | 3.01 | 🟢 Normal | -0.052 |  |
| 2026-10-06 11:04:25 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.189 |  |
| 2026-10-06 11:04:25 | Dunamale (Aththanagalu Oya) | 2.44 | 🟢 Normal | -0.041 |  |
| 2026-10-06 11:04:06 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-06 11:04:02 | Hanwella (Kelani Ganga) | 3.79 | 🟢 Normal | -0.131 |  |
| 2026-10-06 11:03:41 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.061 |  |
| 2026-10-06 11:02:49 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | -0.050 |  |
| 2026-10-06 11:02:46 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.049 |  |
| 2026-10-06 11:02:41 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-10-06 11:02:26 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.051 |  |
| 2026-10-06 11:02:11 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-06 11:02:07 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-10-06 11:01:55 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-06 11:01:47 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | -0.160 |  |
| 2026-10-06 11:01:45 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 11:01:43 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-10-06 11:01:40 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.011 |  |
| 2026-10-06 11:01:20 | Siyambalanduwa (Heda Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-06 11:01:13 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-10-06 11:01:11 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-06 11:01:10 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.229 |  |
| 2026-10-06 11:01:04 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-10-06 11:00:57 | Thanthirimale (Malwathu Oya) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 11:00:57 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 11:17:44 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-10-06 11:09:05 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-06 11:05:50 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-06 11:00:57 | Thanthirimale (Malwathu Oya) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 11:00:34 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-06 11:05:43 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-06 11:01:45 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 11:01:11 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-06 11:02:11 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-06 11:10:53 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-06 11:01:20 | Siyambalanduwa (Heda Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-06 11:01:55 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-06 11:19:17 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-06 11:07:35 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-06 11:05:17 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-10-06 11:01:04 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-10-06 11:10:16 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-10-06 11:01:43 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-10-06 11:02:07 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-10-06 11:01:13 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-10-06 11:02:41 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-10-06 11:00:57 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-10-06 11:01:40 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.011 |  |
| 2026-10-06 10:01:06 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-10-06 11:07:02 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-10-06 11:30:07 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.024 |  |
| 2026-10-06 11:05:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.87 | 🟢 Normal | -0.038 |  |
| 2026-10-06 11:04:25 | Dunamale (Aththanagalu Oya) | 2.44 | 🟢 Normal | -0.041 |  |
| 2026-10-06 11:02:46 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.049 |  |
| 2026-10-06 11:16:42 | Panadugama (Nilwala Ganga) | 3.78 | 🟢 Normal | -0.050 |  |
| 2026-10-06 11:02:49 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | -0.050 |  |
| 2026-10-06 11:02:26 | Giriulla (Maha Oya) | 1.68 | 🟢 Normal | -0.051 |  |
| 2026-10-06 11:04:37 | Badalgama (Maha Oya) | 3.01 | 🟢 Normal | -0.052 |  |
| 2026-10-06 11:03:41 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.061 |  |
| 2026-10-06 11:05:00 | Glencourse (Kelani Ganga) | 11.48 | 🟢 Normal | -0.095 |  |
| 2026-10-06 11:04:02 | Hanwella (Kelani Ganga) | 3.79 | 🟢 Normal | -0.131 |  |
| 2026-10-06 11:01:47 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | -0.160 |  |
| 2026-10-06 11:04:25 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.189 |  |
| 2026-10-06 11:01:10 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.229 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)