# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--11_10:29:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **284,859 measurements** from **39** stations.
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
| 2026-10-11 10:29:20 | Panadugama (Nilwala Ganga) | 3.99 | 🟢 Normal | 0.000 |  |
| 2026-10-11 10:19:43 | Magura (Kalu Ganga) | 3.22 | 🟢 Normal | -0.154 |  |
| 2026-10-11 10:12:43 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.043 |  |
| 2026-10-11 10:09:21 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.035 |  |
| 2026-10-11 10:09:19 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-10-11 10:07:39 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-10-11 10:07:02 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.014 |  |
| 2026-10-11 10:07:01 | Rathnapura (Kalu Ganga) | 2.27 | 🟢 Normal | -0.050 |  |
| 2026-10-11 10:06:49 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-11 10:06:20 | Thanamalwila (Kirindi Oya) | 1.44 | 🟢 Normal | -0.048 |  |
| 2026-10-11 10:06:09 | Glencourse (Kelani Ganga) | 10.96 | 🟢 Normal | -0.020 |  |
| 2026-10-11 10:06:03 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-11 10:05:52 | Peradeniya (Mahaweli Ganga) | 2.97 | 🟢 Normal | -0.009 |  |
| 2026-10-11 10:05:28 | Dunamale (Aththanagalu Oya) | 2.96 | 🟢 Normal | -0.061 |  |
| 2026-10-11 10:05:06 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.109 |  |
| 2026-10-11 10:04:57 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-10-11 10:04:28 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 10:04:15 | Baddegama (Gin Ganga) | 2.32 | 🟢 Normal | -0.022 |  |
| 2026-10-11 10:04:09 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.021 |  |
| 2026-10-11 10:03:59 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-10-11 10:03:58 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.099 |  |
| 2026-10-11 10:03:57 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-11 10:03:53 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.049 |  |
| 2026-10-11 10:03:44 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 10:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 10:03:27 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 10:03:17 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-11 10:03:17 | Giriulla (Maha Oya) | 2.65 | 🟢 Normal | -0.079 |  |
| 2026-10-11 10:03:12 | Moragaswewa (Deduru Oya) | 2.58 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-10-11 10:02:17 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 10:02:14 | Hanwella (Kelani Ganga) | 2.94 | 🟢 Normal | -0.043 |  |
| 2026-10-11 10:02:12 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.237 |  |
| 2026-10-11 10:02:05 | Badalgama (Maha Oya) | 3.88 | 🟢 Normal | -0.061 |  |
| 2026-10-11 10:01:57 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.032 |  |
| 2026-10-11 10:01:32 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.041 |  |
| 2026-10-11 10:01:25 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-10-11 10:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-11 10:01:11 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-10-11 10:00:27 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 10:03:12 | Moragaswewa (Deduru Oya) | 2.58 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-10-11 10:06:03 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-11 10:09:19 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-10-11 10:06:49 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-11 10:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 10:03:27 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 10:02:17 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 10:03:17 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-11 10:04:28 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 10:29:20 | Panadugama (Nilwala Ganga) | 3.99 | 🟢 Normal | 0.000 |  |
| 2026-10-11 10:03:44 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 10:03:59 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-10-11 10:03:57 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-11 10:05:52 | Peradeniya (Mahaweli Ganga) | 2.97 | 🟢 Normal | -0.009 |  |
| 2026-10-11 10:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-11 10:04:57 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-10-11 10:07:39 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-10-11 10:01:25 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-10-11 10:07:02 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.014 |  |
| 2026-10-11 10:06:09 | Glencourse (Kelani Ganga) | 10.96 | 🟢 Normal | -0.020 |  |
| 2026-10-11 10:04:09 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.021 |  |
| 2026-10-11 10:04:15 | Baddegama (Gin Ganga) | 2.32 | 🟢 Normal | -0.022 |  |
| 2026-10-11 10:00:27 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.030 |  |
| 2026-10-11 10:01:11 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-10-11 10:01:57 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.032 |  |
| 2026-10-11 10:09:21 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.035 |  |
| 2026-10-11 10:01:32 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.041 |  |
| 2026-10-11 10:02:14 | Hanwella (Kelani Ganga) | 2.94 | 🟢 Normal | -0.043 |  |
| 2026-10-11 10:12:43 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.043 |  |
| 2026-10-11 10:06:20 | Thanamalwila (Kirindi Oya) | 1.44 | 🟢 Normal | -0.048 |  |
| 2026-10-11 10:03:53 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.049 |  |
| 2026-10-11 10:07:01 | Rathnapura (Kalu Ganga) | 2.27 | 🟢 Normal | -0.050 |  |
| 2026-10-11 10:02:05 | Badalgama (Maha Oya) | 3.88 | 🟢 Normal | -0.061 |  |
| 2026-10-11 10:05:28 | Dunamale (Aththanagalu Oya) | 2.96 | 🟢 Normal | -0.061 |  |
| 2026-10-11 10:03:17 | Giriulla (Maha Oya) | 2.65 | 🟢 Normal | -0.079 |  |
| 2026-10-11 10:03:58 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.099 |  |
| 2026-10-11 10:05:06 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.109 |  |
| 2026-10-11 10:19:43 | Magura (Kalu Ganga) | 3.22 | 🟢 Normal | -0.154 |  |
| 2026-10-11 10:02:12 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.237 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)