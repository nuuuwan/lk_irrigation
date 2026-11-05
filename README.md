# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--05_10:03:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,399 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 10:03:17 | Hanwella (Kelani Ganga) | 2.69 | 🟢 Normal | -0.030 |  |
| 2026-11-05 10:03:16 | Panadugama (Nilwala Ganga) | 4.59 | 🟢 Normal | -0.064 |  |
| 2026-11-05 10:03:09 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | -0.121 |  |
| 2026-11-05 10:03:06 | Urawa (Nilwala Ganga) | 1.63 | 🟢 Normal | -0.113 |  |
| 2026-11-05 10:03:06 | Pitabeddara (Nilwala Ganga) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-11-05 10:03:05 | Ellagawa (Kalu Ganga) | 6.24 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-05 10:02:59 | Giriulla (Maha Oya) | 2.27 | 🟢 Normal | -0.029 |  |
| 2026-11-05 10:02:55 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.021 |  |
| 2026-11-05 10:02:51 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.397 | 🔺 Rising |
| 2026-11-05 10:02:39 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.119 |  |
| 2026-11-05 10:02:39 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-05 10:02:31 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-11-05 10:02:28 | Wellawaya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-11-05 10:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.20 | 🟡 Alert | 0.000 |  |
| 2026-11-05 10:02:09 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-05 10:01:53 | Dunamale (Aththanagalu Oya) | 2.83 | 🟢 Normal | -0.061 |  |
| 2026-11-05 10:01:36 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 10:01:21 | Thanamalwila (Kirindi Oya) | 2.14 | 🟢 Normal | -0.057 |  |
| 2026-11-05 10:01:11 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-11-05 10:01:05 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.015 |  |
| 2026-11-05 10:00:58 | Moraketiya (Walawe Ganga) | 2.15 | 🟢 Normal | -0.084 |  |
| 2026-11-05 10:00:52 | Kuda Oya (Kirindi Oya) | 2.47 | 🟢 Normal | -0.035 |  |
| 2026-11-05 10:00:51 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | -0.011 |  |
| 2026-11-05 10:00:32 | Weraganthota (Mahaweli Ganga) | -2.57 | 🟢 Normal | 0.214 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 10:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.20 | 🟡 Alert | 0.000 |  |
| 2026-11-05 10:02:51 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.397 | 🔺 Rising |
| 2026-11-05 09:01:10 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-11-05 10:00:32 | Weraganthota (Mahaweli Ganga) | -2.57 | 🟢 Normal | 0.214 | 🔺 Rising |
| 2026-11-05 09:06:22 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-05 09:04:22 | Rathnapura (Kalu Ganga) | 3.79 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-11-05 10:03:05 | Ellagawa (Kalu Ganga) | 6.24 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-05 09:03:28 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-05 10:01:36 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 10:02:09 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-05 09:04:46 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-11-05 09:07:17 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 09:03:42 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.000 |  |
| 2026-11-05 10:02:39 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-05 08:01:01 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-05 08:15:45 | Thalgahagoda (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.005 |  |
| 2026-11-05 10:02:31 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-11-05 10:02:28 | Wellawaya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-11-05 09:01:31 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-05 10:00:51 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | -0.011 |  |
| 2026-11-05 09:05:02 | Holombuwa (Kelani Ganga) | 1.03 | 🟢 Normal | -0.012 |  |
| 2026-11-05 10:01:05 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.015 |  |
| 2026-11-05 10:03:06 | Pitabeddara (Nilwala Ganga) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-11-05 10:02:55 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.021 |  |
| 2026-11-05 10:02:59 | Giriulla (Maha Oya) | 2.27 | 🟢 Normal | -0.029 |  |
| 2026-11-05 10:03:17 | Hanwella (Kelani Ganga) | 2.69 | 🟢 Normal | -0.030 |  |
| 2026-11-05 10:01:11 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-11-05 10:00:52 | Kuda Oya (Kirindi Oya) | 2.47 | 🟢 Normal | -0.035 |  |
| 2026-11-05 09:02:36 | Moragaswewa (Deduru Oya) | 3.63 | 🟢 Normal | -0.043 |  |
| 2026-11-05 09:06:12 | Badalgama (Maha Oya) | 3.59 | 🟢 Normal | -0.051 |  |
| 2026-11-05 10:01:21 | Thanamalwila (Kirindi Oya) | 2.14 | 🟢 Normal | -0.057 |  |
| 2026-11-05 10:01:53 | Dunamale (Aththanagalu Oya) | 2.83 | 🟢 Normal | -0.061 |  |
| 2026-11-05 10:03:16 | Panadugama (Nilwala Ganga) | 4.59 | 🟢 Normal | -0.064 |  |
| 2026-11-05 09:06:55 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.066 |  |
| 2026-11-05 10:00:58 | Moraketiya (Walawe Ganga) | 2.15 | 🟢 Normal | -0.084 |  |
| 2026-11-05 09:08:31 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.094 |  |
| 2026-11-05 10:03:06 | Urawa (Nilwala Ganga) | 1.63 | 🟢 Normal | -0.113 |  |
| 2026-11-05 10:02:39 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.119 |  |
| 2026-11-05 10:03:09 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)