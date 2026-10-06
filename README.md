# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--07_01:05:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **280,926 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 01:05:23 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-07 01:04:47 | Baddegama (Gin Ganga) | 1.89 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-07 01:04:40 | Thawalama (Gin Ganga) | 2.68 | 🟢 Normal | -0.037 |  |
| 2026-10-07 01:03:58 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-07 01:03:48 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-07 01:03:45 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-07 01:03:33 | Peradeniya (Mahaweli Ganga) | 3.04 | 🟢 Normal | -0.020 |  |
| 2026-10-07 01:03:29 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-07 01:03:27 | Katharagama (Menik Ganga) | 0.25 | 🟢 Normal | 0.512 | 🔺 Rising |
| 2026-10-07 01:02:59 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.011 |  |
| 2026-10-07 01:02:48 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-07 01:02:32 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-07 01:02:30 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-07 01:02:25 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-10-07 01:02:08 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | -0.082 |  |
| 2026-10-07 01:02:02 | Panadugama (Nilwala Ganga) | 5.06 | 🟡 Alert | 0.345 | 🔺 Rising |
| 2026-10-07 01:01:53 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 01:01:44 | Ellagawa (Kalu Ganga) | 5.57 | 🟢 Normal | -0.051 |  |
| 2026-10-07 01:01:34 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-07 01:01:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.28 | 🟢 Normal | -0.020 |  |
| 2026-10-07 01:01:21 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-07 01:01:01 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-10-07 01:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-10-07 01:00:13 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 0.000 |  |
| 2026-10-07 00:50:29 | Hanwella (Kelani Ganga) | 2.30 | 🟢 Normal | -0.714 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 01:02:02 | Panadugama (Nilwala Ganga) | 5.06 | 🟡 Alert | 0.345 | 🔺 Rising |
| 2026-10-07 00:03:37 | Pitabeddara (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.631 | 🔺 Rising |
| 2026-10-07 01:03:27 | Katharagama (Menik Ganga) | 0.25 | 🟢 Normal | 0.512 | 🔺 Rising |
| 2026-10-07 01:02:25 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-10-07 01:03:29 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-07 01:03:45 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-06 23:06:14 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-10-07 01:05:23 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-07 01:04:47 | Baddegama (Gin Ganga) | 1.89 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-07 00:05:34 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-07 00:14:49 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-07 00:00:39 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 00:01:09 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.005 |  |
| 2026-10-07 01:02:32 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-07 01:02:48 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-07 01:01:53 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 01:01:01 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:03:52 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-07 01:03:58 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-07 00:01:59 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 01:03:48 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-07 01:00:13 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 0.000 |  |
| 2026-10-07 01:01:34 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-06 18:01:28 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-07 01:01:21 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-07 01:02:30 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-07 00:06:59 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.009 |  |
| 2026-10-07 01:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-10-07 01:02:59 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.011 |  |
| 2026-10-06 18:01:43 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.011 |  |
| 2026-10-07 00:05:33 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.019 |  |
| 2026-10-07 01:01:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.28 | 🟢 Normal | -0.020 |  |
| 2026-10-07 01:03:33 | Peradeniya (Mahaweli Ganga) | 3.04 | 🟢 Normal | -0.020 |  |
| 2026-10-07 00:02:28 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.030 |  |
| 2026-10-07 01:04:40 | Thawalama (Gin Ganga) | 2.68 | 🟢 Normal | -0.037 |  |
| 2026-10-07 01:01:44 | Ellagawa (Kalu Ganga) | 5.57 | 🟢 Normal | -0.051 |  |
| 2026-10-07 01:02:08 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | -0.082 |  |
| 2026-10-07 00:08:57 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.082 |  |
| 2026-10-07 00:50:29 | Hanwella (Kelani Ganga) | 2.30 | 🟢 Normal | -0.714 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)