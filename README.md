# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--10_23:19:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **284,453 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 23:19:31 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-10-10 23:17:53 | Putupaula (Kalu Ganga) | 1.06 | 🟢 Normal | -0.036 |  |
| 2026-10-10 23:17:30 | Panadugama (Nilwala Ganga) | 4.12 | 🟢 Normal | -0.010 |  |
| 2026-10-10 23:15:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.97 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-10 23:12:55 | Rathnapura (Kalu Ganga) | 2.27 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-10 23:10:25 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-10 23:10:21 | Giriulla (Maha Oya) | 2.89 | 🟢 Normal | -0.020 |  |
| 2026-10-10 23:09:56 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-10 23:09:22 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-10 23:08:44 | Magura (Kalu Ganga) | 2.98 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-10-10 23:08:43 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-10-10 23:07:41 | Thawalama (Gin Ganga) | 2.96 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-10 23:06:01 | Thaldena (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.098 |  |
| 2026-10-10 23:05:32 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 23:05:10 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-10 23:05:09 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-10-10 23:04:31 | Badalgama (Maha Oya) | 3.81 | 🟢 Normal | -0.030 |  |
| 2026-10-10 23:03:58 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-10 23:03:54 | Hanwella (Kelani Ganga) | 2.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 23:03:04 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-10-10 23:02:53 | Moragaswewa (Deduru Oya) | 2.30 | 🟢 Normal | 1.993 | 🔺 Rising |
| 2026-10-10 23:02:45 | Nakkala (Kumbukkan Oya) | 2.03 | 🟢 Normal | -0.309 |  |
| 2026-10-10 23:02:44 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-10 23:02:43 | Norwood (Kelani Ganga) | 1.40 | 🟢 Normal | -0.150 |  |
| 2026-10-10 23:02:23 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-10 23:02:22 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-10-10 23:01:51 | Ellagawa (Kalu Ganga) | 6.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 23:01:38 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 23:01:33 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-10 23:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-10 23:01:02 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-10 23:00:21 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-10 23:00:16 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.050 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 23:02:53 | Moragaswewa (Deduru Oya) | 2.30 | 🟢 Normal | 1.993 | 🔺 Rising |
| 2026-10-10 23:08:43 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-10-10 23:08:44 | Magura (Kalu Ganga) | 2.98 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-10-10 23:19:31 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-10-10 23:07:41 | Thawalama (Gin Ganga) | 2.96 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-10 23:10:25 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-10 22:05:20 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-10 23:15:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.97 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-10 23:00:16 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-10 23:01:33 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-10 23:02:23 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-10 23:05:10 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-10 23:00:21 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-10 23:02:44 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-10 23:12:55 | Rathnapura (Kalu Ganga) | 2.27 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-10 23:05:32 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 23:03:54 | Hanwella (Kelani Ganga) | 2.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 23:01:51 | Ellagawa (Kalu Ganga) | 6.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 23:01:38 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 23:01:02 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:01:26 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-10 23:03:58 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-10 23:09:56 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:00:50 | Thanthirimale (Malwathu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-10 23:09:22 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-10 23:17:30 | Panadugama (Nilwala Ganga) | 4.12 | 🟢 Normal | -0.010 |  |
| 2026-10-10 23:05:09 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-10-10 23:03:04 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-10-10 23:02:22 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-10-10 23:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-10 23:10:21 | Giriulla (Maha Oya) | 2.89 | 🟢 Normal | -0.020 |  |
| 2026-10-10 22:05:40 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.024 |  |
| 2026-10-10 23:04:31 | Badalgama (Maha Oya) | 3.81 | 🟢 Normal | -0.030 |  |
| 2026-10-10 23:17:53 | Putupaula (Kalu Ganga) | 1.06 | 🟢 Normal | -0.036 |  |
| 2026-10-10 18:05:26 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.050 |  |
| 2026-10-10 23:06:01 | Thaldena (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.098 |  |
| 2026-10-10 23:02:43 | Norwood (Kelani Ganga) | 1.40 | 🟢 Normal | -0.150 |  |
| 2026-10-10 22:02:30 | Peradeniya (Mahaweli Ganga) | 3.65 | 🟢 Normal | -0.305 |  |
| 2026-10-10 23:02:45 | Nakkala (Kumbukkan Oya) | 2.03 | 🟢 Normal | -0.309 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)