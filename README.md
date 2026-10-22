# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--22_13:12:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **294,904 measurements** from **39** stations.
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
| 2026-10-22 13:12:13 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-22 13:11:51 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-10-22 13:09:58 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.009 |  |
| 2026-10-22 13:09:03 | Holombuwa (Kelani Ganga) | 1.33 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-22 13:08:59 | Manampitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-22 13:08:53 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | -0.133 |  |
| 2026-10-22 13:08:10 | Badalgama (Maha Oya) | 3.70 | 🟢 Normal | -0.059 |  |
| 2026-10-22 13:06:53 | Panadugama (Nilwala Ganga) | 4.30 | 🟢 Normal | -0.028 |  |
| 2026-10-22 13:06:29 | Hanwella (Kelani Ganga) | 4.39 | 🟢 Normal | -0.078 |  |
| 2026-10-22 13:05:55 | Peradeniya (Mahaweli Ganga) | 3.02 | 🟢 Normal | -0.028 |  |
| 2026-10-22 13:05:47 | Thanthirimale (Malwathu Oya) | 2.10 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-22 13:05:32 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-22 13:05:31 | Putupaula (Kalu Ganga) | 1.38 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-22 13:05:21 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.019 |  |
| 2026-10-22 13:05:06 | Dunamale (Aththanagalu Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 13:04:50 | Glencourse (Kelani Ganga) | 12.03 | 🟢 Normal | -0.099 |  |
| 2026-10-22 13:04:42 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 13:04:33 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.289 |  |
| 2026-10-22 13:04:21 | Rathnapura (Kalu Ganga) | 4.37 | 🟢 Normal | -0.161 |  |
| 2026-10-22 13:04:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 13:04:17 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.009 |  |
| 2026-10-22 13:04:03 | Ellagawa (Kalu Ganga) | 7.52 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-22 13:04:01 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-10-22 13:03:28 | Galgamuwa (Mee Oya) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 13:03:19 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-10-22 13:03:14 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-10-22 13:03:11 | Moragaswewa (Deduru Oya) | 4.26 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-22 13:02:55 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-10-22 13:02:41 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | -0.019 |  |
| 2026-10-22 13:02:36 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 13:02:26 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-10-22 13:02:07 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-10-22 13:02:01 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-22 13:01:40 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-10-22 13:01:28 | Horowpothana (Yan Oya) | 3.16 | 🟢 Normal | -0.107 |  |
| 2026-10-22 13:01:06 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | -0.011 |  |
| 2026-10-22 13:00:47 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.072 |  |
| 2026-10-22 13:00:08 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 13:11:51 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-10-22 13:03:11 | Moragaswewa (Deduru Oya) | 4.26 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-22 13:09:03 | Holombuwa (Kelani Ganga) | 1.33 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-22 12:10:47 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-10-22 13:04:03 | Ellagawa (Kalu Ganga) | 7.52 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-22 13:05:31 | Putupaula (Kalu Ganga) | 1.38 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-22 13:08:59 | Manampitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-22 13:02:01 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-22 13:05:47 | Thanthirimale (Malwathu Oya) | 2.10 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-22 13:04:42 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 13:05:32 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-22 13:03:28 | Galgamuwa (Mee Oya) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 13:04:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 13:02:26 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-10-22 13:02:07 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-10-22 13:05:06 | Dunamale (Aththanagalu Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 13:02:36 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-22 13:12:13 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-22 13:09:58 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.009 |  |
| 2026-10-22 13:04:17 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.009 |  |
| 2026-10-22 13:03:14 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-10-22 13:02:55 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-10-22 13:03:19 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-10-22 13:04:01 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-10-22 13:01:06 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | -0.011 |  |
| 2026-10-22 13:05:21 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.019 |  |
| 2026-10-22 13:02:41 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | -0.019 |  |
| 2026-10-22 13:01:40 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-10-22 13:00:08 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.021 |  |
| 2026-10-22 13:05:55 | Peradeniya (Mahaweli Ganga) | 3.02 | 🟢 Normal | -0.028 |  |
| 2026-10-22 13:06:53 | Panadugama (Nilwala Ganga) | 4.30 | 🟢 Normal | -0.028 |  |
| 2026-10-22 13:08:10 | Badalgama (Maha Oya) | 3.70 | 🟢 Normal | -0.059 |  |
| 2026-10-22 13:00:47 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.072 |  |
| 2026-10-22 13:06:29 | Hanwella (Kelani Ganga) | 4.39 | 🟢 Normal | -0.078 |  |
| 2026-10-22 13:04:50 | Glencourse (Kelani Ganga) | 12.03 | 🟢 Normal | -0.099 |  |
| 2026-10-22 13:01:28 | Horowpothana (Yan Oya) | 3.16 | 🟢 Normal | -0.107 |  |
| 2026-10-22 13:08:53 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | -0.133 |  |
| 2026-10-22 13:04:21 | Rathnapura (Kalu Ganga) | 4.37 | 🟢 Normal | -0.161 |  |
| 2026-10-22 13:04:33 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.289 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)