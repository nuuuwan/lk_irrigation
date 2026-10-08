# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--08_14:17:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **282,328 measurements** from **39** stations.
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
| 2026-10-08 14:17:10 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-08 14:10:31 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-10-08 14:09:12 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.039 |  |
| 2026-10-08 14:09:11 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | -0.030 |  |
| 2026-10-08 14:08:00 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | -0.022 |  |
| 2026-10-08 14:07:28 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.009 |  |
| 2026-10-08 14:06:31 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-08 14:06:11 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-08 14:06:11 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-08 14:05:31 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-08 14:05:24 | Ellagawa (Kalu Ganga) | 5.29 | 🟢 Normal | -0.010 |  |
| 2026-10-08 14:05:23 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-08 14:05:12 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.022 |  |
| 2026-10-08 14:05:07 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-08 14:04:55 | Badalgama (Maha Oya) | 3.21 | 🟢 Normal | -0.093 |  |
| 2026-10-08 14:04:45 | Glencourse (Kelani Ganga) | 10.94 | 🟢 Normal | -0.078 |  |
| 2026-10-08 14:03:52 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-08 14:03:44 | Giriulla (Maha Oya) | 1.77 | 🟢 Normal | -0.079 |  |
| 2026-10-08 14:03:00 | Dunamale (Aththanagalu Oya) | 2.59 | 🟢 Normal | -0.113 |  |
| 2026-10-08 14:02:52 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | -0.060 |  |
| 2026-10-08 14:02:46 | Nagalagam Street (Kelani Ganga) | 0.78 | 🟢 Normal | -0.015 |  |
| 2026-10-08 14:02:44 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-10-08 14:02:38 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-08 14:02:35 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-08 14:02:33 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-08 14:02:31 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-08 14:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.50 | 🟢 Normal | -0.061 |  |
| 2026-10-08 14:02:04 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.011 |  |
| 2026-10-08 14:01:41 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-08 14:01:27 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.082 |  |
| 2026-10-08 14:01:27 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 14:01:24 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 14:01:24 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-08 14:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-08 14:01:08 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | -0.010 |  |
| 2026-10-08 14:00:46 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-08 14:00:35 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-08 14:00:04 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 14:10:31 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-10-08 14:05:23 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-08 14:02:35 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-08 14:06:31 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-08 14:02:33 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-08 14:03:52 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-08 14:05:07 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-08 14:01:24 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-08 14:01:27 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 14:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-08 14:00:35 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-08 14:00:04 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-08 14:05:31 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-08 14:06:11 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-08 13:16:50 | Baddegama (Gin Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-08 14:01:24 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 14:02:31 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-08 14:06:11 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-08 14:00:46 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-08 14:17:10 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-08 14:02:38 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-08 14:01:41 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-08 14:07:28 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.009 |  |
| 2026-10-08 14:02:44 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-10-08 14:05:24 | Ellagawa (Kalu Ganga) | 5.29 | 🟢 Normal | -0.010 |  |
| 2026-10-08 14:01:08 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | -0.010 |  |
| 2026-10-08 14:02:04 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.011 |  |
| 2026-10-08 14:02:46 | Nagalagam Street (Kelani Ganga) | 0.78 | 🟢 Normal | -0.015 |  |
| 2026-10-08 14:08:00 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | -0.022 |  |
| 2026-10-08 14:05:12 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.022 |  |
| 2026-10-08 14:09:11 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | -0.030 |  |
| 2026-10-08 14:09:12 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.039 |  |
| 2026-10-08 14:02:52 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | -0.060 |  |
| 2026-10-08 14:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.50 | 🟢 Normal | -0.061 |  |
| 2026-10-08 14:04:45 | Glencourse (Kelani Ganga) | 10.94 | 🟢 Normal | -0.078 |  |
| 2026-10-08 14:03:44 | Giriulla (Maha Oya) | 1.77 | 🟢 Normal | -0.079 |  |
| 2026-10-08 14:01:27 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.082 |  |
| 2026-10-08 14:04:55 | Badalgama (Maha Oya) | 3.21 | 🟢 Normal | -0.093 |  |
| 2026-10-08 14:03:00 | Dunamale (Aththanagalu Oya) | 2.59 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)