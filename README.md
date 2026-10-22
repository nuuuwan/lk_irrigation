# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--22_09:08:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **294,744 measurements** from **39** stations.
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
| 2026-10-22 09:08:37 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.022 |  |
| 2026-10-22 09:08:35 | Horowpothana (Yan Oya) | 3.20 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-22 09:08:33 | Thalgahagoda (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.036 |  |
| 2026-10-22 09:08:25 | Pitabeddara (Nilwala Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-22 09:08:17 | Putupaula (Kalu Ganga) | 1.11 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-10-22 09:07:47 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-22 09:06:55 | Badalgama (Maha Oya) | 3.49 | 🟢 Normal | 2.455 | 🔺 Rising |
| 2026-10-22 09:06:22 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-22 09:05:39 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.078 |  |
| 2026-10-22 09:05:09 | Glencourse (Kelani Ganga) | 12.68 | 🟢 Normal | -0.203 |  |
| 2026-10-22 09:04:43 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-10-22 09:04:43 | Badalgama (Maha Oya) | 3.40 | 🟢 Normal | 2.455 | 🔺 Rising |
| 2026-10-22 09:04:30 | Hanwella (Kelani Ganga) | 4.69 | 🟢 Normal | -0.010 |  |
| 2026-10-22 09:04:25 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-10-22 09:04:15 | Pitabeddara (Nilwala Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-22 09:04:07 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.020 |  |
| 2026-10-22 09:04:02 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-22 09:03:55 | Panadugama (Nilwala Ganga) | 4.46 | 🟢 Normal | -0.070 |  |
| 2026-10-22 09:03:41 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-22 09:03:28 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-10-22 09:03:24 | Peradeniya (Mahaweli Ganga) | 3.18 | 🟢 Normal | -0.128 |  |
| 2026-10-22 09:03:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.37 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-22 09:03:16 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | -0.097 |  |
| 2026-10-22 09:03:03 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 09:03:00 | Ellagawa (Kalu Ganga) | 7.32 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-10-22 09:02:57 | Giriulla (Maha Oya) | 2.68 | 🟢 Normal | -0.030 |  |
| 2026-10-22 09:02:45 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | -0.031 |  |
| 2026-10-22 09:02:45 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | -0.019 |  |
| 2026-10-22 09:02:41 | Rathnapura (Kalu Ganga) | 5.11 | 🟢 Normal | -0.072 |  |
| 2026-10-22 09:02:39 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 09:02:30 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-22 09:02:11 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-22 09:01:57 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-10-22 09:01:38 | Moragaswewa (Deduru Oya) | 4.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 09:01:37 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-10-22 09:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-10-22 09:01:08 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | -0.099 |  |
| 2026-10-22 09:00:55 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | -0.021 |  |
| 2026-10-22 09:00:42 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.168 |  |
| 2026-10-22 08:35:16 | Thalgahagoda (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.036 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 09:06:55 | Badalgama (Maha Oya) | 3.49 | 🟢 Normal | 2.455 | 🔺 Rising |
| 2026-10-22 09:03:00 | Ellagawa (Kalu Ganga) | 7.32 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-10-22 09:07:47 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-22 09:08:17 | Putupaula (Kalu Ganga) | 1.11 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-10-22 09:04:02 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-22 09:03:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.37 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-22 09:03:41 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-22 09:02:30 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-22 09:02:11 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-22 09:03:03 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 09:01:38 | Moragaswewa (Deduru Oya) | 4.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 09:08:35 | Horowpothana (Yan Oya) | 3.20 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-22 09:08:25 | Pitabeddara (Nilwala Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-22 09:06:22 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-22 09:04:25 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-10-22 09:02:39 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 08:19:52 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-22 09:04:30 | Hanwella (Kelani Ganga) | 4.69 | 🟢 Normal | -0.010 |  |
| 2026-10-22 09:01:37 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-10-22 09:01:57 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-10-22 08:03:33 | Galgamuwa (Mee Oya) | 2.26 | 🟢 Normal | -0.011 |  |
| 2026-10-22 09:02:45 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | -0.019 |  |
| 2026-10-22 09:04:43 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-10-22 09:04:07 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.020 |  |
| 2026-10-22 09:00:55 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | -0.021 |  |
| 2026-10-22 09:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-10-22 09:08:37 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.022 |  |
| 2026-10-22 09:03:28 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-10-22 09:02:57 | Giriulla (Maha Oya) | 2.68 | 🟢 Normal | -0.030 |  |
| 2026-10-22 09:02:45 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | -0.031 |  |
| 2026-10-22 09:08:33 | Thalgahagoda (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.036 |  |
| 2026-10-22 09:03:55 | Panadugama (Nilwala Ganga) | 4.46 | 🟢 Normal | -0.070 |  |
| 2026-10-22 09:02:41 | Rathnapura (Kalu Ganga) | 5.11 | 🟢 Normal | -0.072 |  |
| 2026-10-22 09:05:39 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.078 |  |
| 2026-10-22 09:03:16 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | -0.097 |  |
| 2026-10-22 09:01:08 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | -0.099 |  |
| 2026-10-22 09:03:24 | Peradeniya (Mahaweli Ganga) | 3.18 | 🟢 Normal | -0.128 |  |
| 2026-10-22 09:00:42 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.168 |  |
| 2026-10-22 09:05:09 | Glencourse (Kelani Ganga) | 12.68 | 🟢 Normal | -0.203 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)