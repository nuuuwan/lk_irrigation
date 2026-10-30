# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--31_02:28:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **302,586 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 02:28:31 | Panadugama (Nilwala Ganga) | 5.03 | 🟡 Alert | -0.007 |  |
| 2026-10-31 02:23:03 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.008 |  |
| 2026-10-31 02:19:53 | Magura (Kalu Ganga) | 2.57 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2026-10-31 02:19:52 | Magura (Kalu Ganga) | 2.52 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2026-10-31 02:11:51 | Baddegama (Gin Ganga) | 2.90 | 🟢 Normal | -0.026 |  |
| 2026-10-31 02:11:37 | Rathnapura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.034 |  |
| 2026-10-31 02:09:45 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-10-31 02:07:39 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | -0.033 |  |
| 2026-10-31 02:06:55 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-31 02:06:53 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-31 02:06:29 | Glencourse (Kelani Ganga) | 10.73 | 🟢 Normal | -0.985 |  |
| 2026-10-31 02:05:22 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.063 |  |
| 2026-10-31 02:05:11 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-10-31 02:04:23 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-31 02:03:53 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.070 |  |
| 2026-10-31 02:03:51 | Putupaula (Kalu Ganga) | 2.95 | 🟢 Normal | -0.059 |  |
| 2026-10-31 02:03:37 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.028 |  |
| 2026-10-31 02:03:36 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-31 02:03:31 | Thalgahagoda (Nilwala Ganga) | 1.76 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-31 02:03:13 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-31 02:03:12 | Yaka Wewa (Ma Oya) | 0.00 | 🟢 Normal | -0.499 |  |
| 2026-10-31 02:03:11 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-31 02:03:08 | Hanwella (Kelani Ganga) | 2.82 | 🟢 Normal | -0.013 |  |
| 2026-10-31 02:03:07 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-31 02:03:06 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-31 02:02:23 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-31 02:01:54 | Thawalama (Gin Ganga) | 2.13 | 🟢 Normal | -0.024 |  |
| 2026-10-31 02:01:52 | Ellagawa (Kalu Ganga) | 7.59 | 🟢 Normal | -0.128 |  |
| 2026-10-31 02:01:48 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-10-31 02:01:42 | Pitabeddara (Nilwala Ganga) | 1.55 | 🟢 Normal | -0.012 |  |
| 2026-10-31 02:01:29 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.040 |  |
| 2026-10-31 02:00:35 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 02:03:31 | Thalgahagoda (Nilwala Ganga) | 1.76 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-31 02:28:31 | Panadugama (Nilwala Ganga) | 5.03 | 🟡 Alert | -0.007 |  |
| 2026-10-31 00:01:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.06 | 🟡 Alert | -0.052 |  |
| 2026-10-31 02:19:53 | Magura (Kalu Ganga) | 2.57 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2026-10-31 02:05:11 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-10-31 02:02:23 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-31 02:03:36 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-31 02:04:23 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-31 02:06:55 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-31 01:01:43 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-31 02:03:06 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-31 02:01:48 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:01:07 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-31 02:03:11 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-31 02:03:07 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-31 02:03:13 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-31 02:06:53 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-31 01:02:40 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-31 00:06:05 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.006 |  |
| 2026-10-31 02:23:03 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.008 |  |
| 2026-10-31 02:09:45 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-10-31 02:01:42 | Pitabeddara (Nilwala Ganga) | 1.55 | 🟢 Normal | -0.012 |  |
| 2026-10-31 02:03:08 | Hanwella (Kelani Ganga) | 2.82 | 🟢 Normal | -0.013 |  |
| 2026-10-30 18:00:09 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.021 |  |
| 2026-10-31 02:00:35 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.021 |  |
| 2026-10-30 18:00:42 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-10-31 02:01:54 | Thawalama (Gin Ganga) | 2.13 | 🟢 Normal | -0.024 |  |
| 2026-10-31 02:11:51 | Baddegama (Gin Ganga) | 2.90 | 🟢 Normal | -0.026 |  |
| 2026-10-31 02:03:37 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.028 |  |
| 2026-10-31 02:07:39 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | -0.033 |  |
| 2026-10-31 02:11:37 | Rathnapura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.034 |  |
| 2026-10-31 02:01:29 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.040 |  |
| 2026-10-31 00:04:18 | Padiyathalawa (Maduru Oya) | 1.38 | 🟢 Normal | -0.049 |  |
| 2026-10-31 02:03:51 | Putupaula (Kalu Ganga) | 2.95 | 🟢 Normal | -0.059 |  |
| 2026-10-31 02:05:22 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.063 |  |
| 2026-10-31 02:03:53 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.070 |  |
| 2026-10-31 02:01:52 | Ellagawa (Kalu Ganga) | 7.59 | 🟢 Normal | -0.128 |  |
| 2026-10-31 02:03:12 | Yaka Wewa (Ma Oya) | 0.00 | 🟢 Normal | -0.499 |  |
| 2026-10-31 02:06:29 | Glencourse (Kelani Ganga) | 10.73 | 🟢 Normal | -0.985 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)