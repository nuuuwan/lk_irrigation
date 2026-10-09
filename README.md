# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--09_23:06:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **283,555 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 23:06:48 | Putupaula (Kalu Ganga) | 1.14 | 🟢 Normal | -0.067 |  |
| 2026-10-09 23:05:45 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-09 23:05:05 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-10-09 23:05:04 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-09 23:04:48 | Urawa (Nilwala Ganga) | 1.46 | 🟢 Normal | -0.155 |  |
| 2026-10-09 23:04:39 | Panadugama (Nilwala Ganga) | 4.26 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-10-09 23:04:16 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.256 | 🔺 Rising |
| 2026-10-09 23:04:16 | Giriulla (Maha Oya) | 3.60 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-09 23:04:11 | Rathnapura (Kalu Ganga) | 3.92 | 🟢 Normal | -0.136 |  |
| 2026-10-09 23:04:02 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-10-09 23:03:33 | Badalgama (Maha Oya) | 4.02 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-10-09 23:03:28 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-09 23:03:27 | Dunamale (Aththanagalu Oya) | 2.65 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-10-09 23:03:22 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.048 |  |
| 2026-10-09 23:03:18 | Norwood (Kelani Ganga) | 1.42 | 🟢 Normal | -0.051 |  |
| 2026-10-09 23:03:07 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-09 23:02:43 | Peradeniya (Mahaweli Ganga) | 4.30 | 🟢 Normal | -0.256 |  |
| 2026-10-09 23:02:20 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-09 23:02:13 | Pitabeddara (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-09 23:02:09 | Glencourse (Kelani Ganga) | 12.48 | 🟢 Normal | -1.440 |  |
| 2026-10-09 23:02:08 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-09 23:02:07 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.011 |  |
| 2026-10-09 23:02:01 | Baddegama (Gin Ganga) | 2.55 | 🟢 Normal | -0.022 |  |
| 2026-10-09 23:01:55 | Moragaswewa (Deduru Oya) | 1.95 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-10-09 23:01:50 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-09 23:01:33 | Ellagawa (Kalu Ganga) | 6.56 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-09 23:01:17 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-09 23:01:06 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-10-09 23:00:57 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-09 23:00:54 | Glencourse (Kelani Ganga) | 12.51 | 🟢 Normal | -1.440 |  |
| 2026-10-09 23:00:49 | Siyambalanduwa (Heda Oya) | 1.18 | 🟢 Normal | 0.732 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 23:00:49 | Siyambalanduwa (Heda Oya) | 1.18 | 🟢 Normal | 0.732 | 🔺 Rising |
| 2026-10-09 23:03:27 | Dunamale (Aththanagalu Oya) | 2.65 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-10-09 23:04:16 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.256 | 🔺 Rising |
| 2026-10-09 23:01:55 | Moragaswewa (Deduru Oya) | 1.95 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-10-09 23:04:39 | Panadugama (Nilwala Ganga) | 4.26 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-10-09 23:01:33 | Ellagawa (Kalu Ganga) | 6.56 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-09 23:02:20 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-09 22:13:19 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-09 23:03:33 | Badalgama (Maha Oya) | 4.02 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-10-09 23:04:16 | Giriulla (Maha Oya) | 3.60 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-09 23:02:13 | Pitabeddara (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-09 23:02:08 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-09 23:03:07 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-09 23:01:50 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-09 18:10:37 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-09 18:01:41 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 23:05:04 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-09 23:05:05 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-10-09 22:02:11 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-09 23:00:57 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-09 22:03:44 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-09 22:03:35 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-10-09 23:01:17 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-09 23:03:28 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:01:04 | Thanthirimale (Malwathu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-09 23:05:45 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-09 23:04:02 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-10-09 23:01:06 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-10-09 23:02:07 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.011 |  |
| 2026-10-09 23:02:01 | Baddegama (Gin Ganga) | 2.55 | 🟢 Normal | -0.022 |  |
| 2026-10-09 22:27:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.30 | 🟢 Normal | -0.041 |  |
| 2026-10-09 23:03:22 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.048 |  |
| 2026-10-09 23:03:18 | Norwood (Kelani Ganga) | 1.42 | 🟢 Normal | -0.051 |  |
| 2026-10-09 23:06:48 | Putupaula (Kalu Ganga) | 1.14 | 🟢 Normal | -0.067 |  |
| 2026-10-09 22:06:42 | Holombuwa (Kelani Ganga) | 1.92 | 🟢 Normal | -0.105 |  |
| 2026-10-09 23:04:11 | Rathnapura (Kalu Ganga) | 3.92 | 🟢 Normal | -0.136 |  |
| 2026-10-09 23:04:48 | Urawa (Nilwala Ganga) | 1.46 | 🟢 Normal | -0.155 |  |
| 2026-10-09 23:02:43 | Peradeniya (Mahaweli Ganga) | 4.30 | 🟢 Normal | -0.256 |  |
| 2026-10-09 23:02:09 | Glencourse (Kelani Ganga) | 12.48 | 🟢 Normal | -1.440 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)