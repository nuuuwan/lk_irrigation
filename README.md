# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--11_11:03:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **312,822 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 11:03:31 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-11-11 11:03:21 | Holombuwa (Kelani Ganga) | 1.23 | 🟢 Normal | -0.011 |  |
| 2026-11-11 11:03:13 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-11-11 11:03:12 | Moraketiya (Walawe Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-11-11 11:02:54 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-11-11 11:02:46 | Kuda Oya (Kirindi Oya) | 1.89 | 🟢 Normal | 1.078 | 🔺 Rising |
| 2026-11-11 11:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.61 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-11 11:02:33 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-11 11:02:33 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-11 11:02:23 | Moragaswewa (Deduru Oya) | 2.68 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-11 11:02:15 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.030 | 🔺 Rising |
| 2026-11-11 11:02:14 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-11 11:02:09 | Ellagawa (Kalu Ganga) | 8.49 | 🟢 Normal | -0.036 |  |
| 2026-11-11 11:01:57 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.022 |  |
| 2026-11-11 11:01:43 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | -0.129 |  |
| 2026-11-11 11:01:19 | Weraganthota (Mahaweli Ganga) | -2.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-11 11:00:52 | Thanthirimale (Malwathu Oya) | 2.03 | 🟢 Normal | -0.020 |  |
| 2026-11-11 11:00:38 | Pitabeddara (Nilwala Ganga) | 1.75 | 🟢 Normal | -0.050 |  |
| 2026-11-11 11:00:07 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.031 |  |
| 2026-11-11 10:58:09 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | -0.045 |  |
| 2026-11-11 10:28:42 | Ellagawa (Kalu Ganga) | 8.51 | 🟢 Normal | -0.036 |  |
| 2026-11-11 10:23:23 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 11:02:15 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.030 | 🔺 Rising |
| 2026-11-11 11:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.61 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-11 10:10:18 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | -0.021 |  |
| 2026-11-11 10:06:26 | Dunamale (Aththanagalu Oya) | 4.14 | 🟡 Alert | -0.028 |  |
| 2026-11-11 10:04:51 | Panadugama (Nilwala Ganga) | 5.70 | 🟡 Alert | -0.063 |  |
| 2026-11-11 11:02:46 | Kuda Oya (Kirindi Oya) | 1.89 | 🟢 Normal | 1.078 | 🔺 Rising |
| 2026-11-11 11:02:23 | Moragaswewa (Deduru Oya) | 2.68 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-11 10:04:25 | Peradeniya (Mahaweli Ganga) | 3.90 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-11 09:59:28 | Padiyathalawa (Maduru Oya) | 0.59 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-11 11:02:33 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-11 11:01:19 | Weraganthota (Mahaweli Ganga) | -2.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-11 10:01:47 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 11:03:13 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-11-11 10:02:21 | Wellawaya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-11 10:07:08 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-11-11 11:02:33 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-11 11:03:12 | Moraketiya (Walawe Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-11-11 11:02:14 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-11 10:05:49 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-11-11 10:11:09 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-11 10:14:57 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | -0.008 |  |
| 2026-11-11 11:03:31 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-11-11 11:02:54 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-11-11 11:03:21 | Holombuwa (Kelani Ganga) | 1.23 | 🟢 Normal | -0.011 |  |
| 2026-11-11 10:06:17 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | -0.019 |  |
| 2026-11-11 11:00:52 | Thanthirimale (Malwathu Oya) | 2.03 | 🟢 Normal | -0.020 |  |
| 2026-11-11 11:01:57 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.022 |  |
| 2026-11-11 10:03:07 | Thanamalwila (Kirindi Oya) | 1.80 | 🟢 Normal | -0.030 |  |
| 2026-11-11 11:00:07 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.031 |  |
| 2026-11-11 11:02:09 | Ellagawa (Kalu Ganga) | 8.49 | 🟢 Normal | -0.036 |  |
| 2026-11-11 10:58:09 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | -0.045 |  |
| 2026-11-11 11:00:38 | Pitabeddara (Nilwala Ganga) | 1.75 | 🟢 Normal | -0.050 |  |
| 2026-11-11 10:12:17 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | -0.067 |  |
| 2026-11-11 10:06:15 | Magura (Kalu Ganga) | 3.19 | 🟢 Normal | -0.094 |  |
| 2026-11-11 10:05:35 | Glencourse (Kelani Ganga) | 11.97 | 🟢 Normal | -0.115 |  |
| 2026-11-11 10:08:37 | Rathnapura (Kalu Ganga) | 4.43 | 🟢 Normal | -0.115 |  |
| 2026-11-11 11:01:43 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | -0.129 |  |
| 2026-11-11 10:05:56 | Hanwella (Kelani Ganga) | 4.58 | 🟢 Normal | -0.135 |  |
| 2026-11-11 10:06:53 | Badalgama (Maha Oya) | 4.15 | 🟢 Normal | -0.143 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)