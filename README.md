# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--25_07:38:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **297,346 measurements** from **39** stations.
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
| 2026-10-25 07:38:07 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-25 07:22:12 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-25 07:18:21 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.016 |  |
| 2026-10-25 07:17:41 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-25 07:17:11 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-25 07:13:23 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-10-25 07:11:54 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.111 |  |
| 2026-10-25 07:08:53 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | -0.101 |  |
| 2026-10-25 07:08:42 | Kithulgala (Kelani Ganga) | 2.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 07:08:40 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.018 |  |
| 2026-10-25 07:07:56 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-10-25 07:07:38 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.004 |  |
| 2026-10-25 07:07:21 | Panadugama (Nilwala Ganga) | 3.96 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-10-25 07:06:33 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 07:05:53 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 07:05:17 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 07:05:07 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-25 07:05:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.89 | 🟢 Normal | -0.010 |  |
| 2026-10-25 07:04:47 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 07:04:42 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-10-25 07:04:25 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-25 07:04:25 | Hanwella (Kelani Ganga) | 2.93 | 🟢 Normal | -0.021 |  |
| 2026-10-25 07:03:42 | Glencourse (Kelani Ganga) | 10.82 | 🟢 Normal | -0.010 |  |
| 2026-10-25 07:03:17 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-10-25 07:03:14 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 07:03:09 | Moragaswewa (Deduru Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-25 07:02:51 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.019 |  |
| 2026-10-25 07:02:50 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-25 07:02:48 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-25 07:02:42 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-10-25 07:02:31 | Ellagawa (Kalu Ganga) | 6.14 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-25 07:02:28 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-10-25 07:02:22 | Rathnapura (Kalu Ganga) | 3.31 | 🟢 Normal | 0.335 | 🔺 Rising |
| 2026-10-25 07:02:12 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 07:01:22 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-10-25 07:01:04 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | -0.026 |  |
| 2026-10-25 07:00:55 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | -0.131 |  |
| 2026-10-25 07:00:55 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.043 |  |
| 2026-10-25 07:00:20 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 07:02:22 | Rathnapura (Kalu Ganga) | 3.31 | 🟢 Normal | 0.335 | 🔺 Rising |
| 2026-10-25 07:07:21 | Panadugama (Nilwala Ganga) | 3.96 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-10-25 07:13:23 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-10-25 07:02:50 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-25 07:02:48 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-25 07:02:31 | Ellagawa (Kalu Ganga) | 6.14 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-25 07:17:11 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-25 07:04:25 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-25 07:08:42 | Kithulgala (Kelani Ganga) | 2.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 07:04:47 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 07:05:53 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 07:06:33 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 07:03:14 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 07:02:12 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 07:05:17 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 07:22:12 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-25 07:03:09 | Moragaswewa (Deduru Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-25 07:00:20 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-25 07:01:22 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-10-25 07:38:07 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-25 07:04:42 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-10-25 07:05:07 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-25 07:17:41 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-25 07:07:38 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.004 |  |
| 2026-10-25 07:07:56 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-10-25 07:03:17 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-10-25 07:02:28 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-10-25 07:03:42 | Glencourse (Kelani Ganga) | 10.82 | 🟢 Normal | -0.010 |  |
| 2026-10-25 07:05:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.89 | 🟢 Normal | -0.010 |  |
| 2026-10-25 07:18:21 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.016 |  |
| 2026-10-25 07:08:40 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.018 |  |
| 2026-10-25 07:02:51 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.019 |  |
| 2026-10-25 07:02:42 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-10-25 07:04:25 | Hanwella (Kelani Ganga) | 2.93 | 🟢 Normal | -0.021 |  |
| 2026-10-25 07:01:04 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | -0.026 |  |
| 2026-10-25 07:00:55 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.043 |  |
| 2026-10-25 07:08:53 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | -0.101 |  |
| 2026-10-25 07:11:54 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.111 |  |
| 2026-10-25 07:00:55 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)