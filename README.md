# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--07_18:12:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **281,585 measurements** from **39** stations.
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
| 2026-10-07 18:12:09 | Panadugama (Nilwala Ganga) | 4.85 | 🟢 Normal | -0.036 |  |
| 2026-10-07 18:10:07 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-10-07 18:09:53 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:08:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.35 | 🟢 Normal | -0.069 |  |
| 2026-10-07 18:07:13 | Baddegama (Gin Ganga) | 2.42 | 🟢 Normal | -0.010 |  |
| 2026-10-07 18:06:25 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-10-07 18:04:59 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | -0.020 |  |
| 2026-10-07 18:04:46 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:04:30 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | -0.021 |  |
| 2026-10-07 18:04:21 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-07 18:04:19 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-10-07 18:04:18 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | -0.009 |  |
| 2026-10-07 18:04:00 | Thawalama (Gin Ganga) | 2.37 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-10-07 18:03:52 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | -0.022 |  |
| 2026-10-07 18:03:30 | Peradeniya (Mahaweli Ganga) | 2.07 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-07 18:03:29 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.047 |  |
| 2026-10-07 18:03:17 | Hanwella (Kelani Ganga) | 2.53 | 🟢 Normal | -0.030 |  |
| 2026-10-07 18:03:15 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:03:09 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-07 18:03:00 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | -0.024 |  |
| 2026-10-07 18:02:57 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-10-07 18:02:42 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-07 18:02:38 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-10-07 18:02:34 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:01:59 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-07 18:01:57 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-07 18:01:57 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:01:49 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-10-07 18:01:45 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.050 |  |
| 2026-10-07 18:01:42 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | -0.051 |  |
| 2026-10-07 18:01:41 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:01:26 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-07 18:01:12 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.052 |  |
| 2026-10-07 18:01:00 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:00:53 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:00:50 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:00:27 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:00:19 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.065 |  |
| 2026-10-07 18:00:17 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 18:02:57 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-10-07 18:04:00 | Thawalama (Gin Ganga) | 2.37 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-10-07 18:02:38 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-10-07 18:03:30 | Peradeniya (Mahaweli Ganga) | 2.07 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-07 18:02:42 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-07 18:04:21 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-07 18:01:57 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-07 18:01:59 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-07 18:03:09 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-07 18:00:53 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:01:41 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:00:27 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:03:15 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:04:46 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:01:00 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:01:57 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:02:34 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:09:53 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:00:50 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:04:18 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | -0.009 |  |
| 2026-10-07 18:06:25 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-10-07 18:01:26 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-07 18:01:49 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-10-07 18:07:13 | Baddegama (Gin Ganga) | 2.42 | 🟢 Normal | -0.010 |  |
| 2026-10-07 18:00:17 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | -0.011 |  |
| 2026-10-07 18:10:07 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-10-07 18:04:59 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | -0.020 |  |
| 2026-10-07 18:04:19 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-10-07 18:04:30 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | -0.021 |  |
| 2026-10-07 18:03:52 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | -0.022 |  |
| 2026-10-07 18:03:00 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | -0.024 |  |
| 2026-10-07 18:03:17 | Hanwella (Kelani Ganga) | 2.53 | 🟢 Normal | -0.030 |  |
| 2026-10-07 18:12:09 | Panadugama (Nilwala Ganga) | 4.85 | 🟢 Normal | -0.036 |  |
| 2026-10-07 18:03:29 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.047 |  |
| 2026-10-07 18:01:45 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.050 |  |
| 2026-10-07 18:01:42 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | -0.051 |  |
| 2026-10-07 18:01:12 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.052 |  |
| 2026-10-07 18:00:19 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.065 |  |
| 2026-10-07 18:08:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.35 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)