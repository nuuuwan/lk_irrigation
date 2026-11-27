# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--27_08:03:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **326,884 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Magura — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 08:03:51 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | -0.021 |  |
| 2026-11-27 08:03:49 | Galgamuwa (Mee Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-11-27 08:03:44 | Dunamale (Aththanagalu Oya) | 3.98 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-27 08:03:25 | Manampitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-11-27 08:03:16 | Hanwella (Kelani Ganga) | 3.54 | 🟢 Normal | -0.052 |  |
| 2026-11-27 08:02:54 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.023 |  |
| 2026-11-27 08:02:53 | Ellagawa (Kalu Ganga) | 6.78 | 🟢 Normal | 0.000 |  |
| 2026-11-27 08:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.31 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-27 08:02:31 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.122 |  |
| 2026-11-27 08:02:28 | Putupaula (Kalu Ganga) | 1.56 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-11-27 08:02:23 | Kuda Oya (Kirindi Oya) | 2.71 | 🟢 Normal | -0.020 |  |
| 2026-11-27 08:02:14 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-11-27 08:02:10 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-11-27 08:02:09 | Thanamalwila (Kirindi Oya) | 2.49 | 🟢 Normal | -0.059 |  |
| 2026-11-27 08:02:07 | Siyambalanduwa (Heda Oya) | 1.48 | 🟢 Normal | -0.268 |  |
| 2026-11-27 08:02:03 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.405 |  |
| 2026-11-27 08:01:51 | Moraketiya (Walawe Ganga) | 3.80 | 🟡 Alert | -0.197 |  |
| 2026-11-27 08:01:50 | Wellawaya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.052 |  |
| 2026-11-27 08:01:33 | Pitabeddara (Nilwala Ganga) | 1.64 | 🟢 Normal | -0.128 |  |
| 2026-11-27 08:01:05 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | -0.011 |  |
| 2026-11-27 08:00:47 | Magura (Kalu Ganga) | 4.58 | 🟡 Alert | -0.112 |  |
| 2026-11-27 08:00:11 | Nakkala (Kumbukkan Oya) | 1.50 | 🟢 Normal | -0.080 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 08:03:44 | Dunamale (Aththanagalu Oya) | 3.98 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-27 08:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.31 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-27 08:00:47 | Magura (Kalu Ganga) | 4.58 | 🟡 Alert | -0.112 |  |
| 2026-11-27 08:01:51 | Moraketiya (Walawe Ganga) | 3.80 | 🟡 Alert | -0.197 |  |
| 2026-11-27 08:02:28 | Putupaula (Kalu Ganga) | 1.56 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-11-27 08:03:25 | Manampitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-11-27 07:07:55 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-27 07:21:44 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-27 07:21:31 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-27 07:15:44 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 08:02:53 | Ellagawa (Kalu Ganga) | 6.78 | 🟢 Normal | 0.000 |  |
| 2026-11-27 07:06:41 | Badalgama (Maha Oya) | 4.98 | 🟢 Normal | 0.000 |  |
| 2026-11-27 07:01:27 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.002 |  |
| 2026-11-27 07:23:16 | Panadugama (Nilwala Ganga) | 4.40 | 🟢 Normal | -0.007 |  |
| 2026-11-27 08:03:49 | Galgamuwa (Mee Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-11-27 08:02:14 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-11-27 08:02:10 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-11-27 08:01:05 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | -0.011 |  |
| 2026-11-27 07:15:40 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.017 |  |
| 2026-11-27 07:10:56 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.017 |  |
| 2026-11-27 08:02:23 | Kuda Oya (Kirindi Oya) | 2.71 | 🟢 Normal | -0.020 |  |
| 2026-11-27 08:03:51 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | -0.021 |  |
| 2026-11-27 08:02:54 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.023 |  |
| 2026-11-27 07:00:58 | Moragaswewa (Deduru Oya) | 3.57 | 🟢 Normal | -0.030 |  |
| 2026-11-27 08:03:16 | Hanwella (Kelani Ganga) | 3.54 | 🟢 Normal | -0.052 |  |
| 2026-11-27 08:01:50 | Wellawaya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.052 |  |
| 2026-11-27 08:02:09 | Thanamalwila (Kirindi Oya) | 2.49 | 🟢 Normal | -0.059 |  |
| 2026-11-27 07:05:25 | Giriulla (Maha Oya) | 4.26 | 🟢 Normal | -0.079 |  |
| 2026-11-27 08:00:11 | Nakkala (Kumbukkan Oya) | 1.50 | 🟢 Normal | -0.080 |  |
| 2026-11-27 07:08:45 | Rathnapura (Kalu Ganga) | 3.00 | 🟢 Normal | -0.088 |  |
| 2026-11-27 08:02:31 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.122 |  |
| 2026-11-27 07:08:52 | Thawalama (Gin Ganga) | 2.76 | 🟢 Normal | -0.122 |  |
| 2026-11-27 08:01:33 | Pitabeddara (Nilwala Ganga) | 1.64 | 🟢 Normal | -0.128 |  |
| 2026-11-27 07:04:10 | Glencourse (Kelani Ganga) | 11.23 | 🟢 Normal | -0.149 |  |
| 2026-11-27 07:06:33 | Holombuwa (Kelani Ganga) | 1.76 | 🟢 Normal | -0.150 |  |
| 2026-11-27 07:05:30 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.256 |  |
| 2026-11-27 08:02:07 | Siyambalanduwa (Heda Oya) | 1.48 | 🟢 Normal | -0.268 |  |
| 2026-11-27 08:02:03 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.405 |  |
| 2026-11-27 07:04:10 | Peradeniya (Mahaweli Ganga) | 4.20 | 🟢 Normal | -324.000 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)