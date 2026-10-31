# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--31_13:03:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **302,990 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 13:03:14 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.031 |  |
| 2026-10-31 13:03:13 | Glencourse (Kelani Ganga) | 10.63 | 🟢 Normal | 0.000 |  |
| 2026-10-31 13:03:06 | Ellagawa (Kalu Ganga) | 6.58 | 🟢 Normal | -0.064 |  |
| 2026-10-31 13:02:48 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-10-31 13:02:46 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-31 13:02:39 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.020 |  |
| 2026-10-31 13:02:38 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.071 |  |
| 2026-10-31 13:02:29 | Thalgahagoda (Nilwala Ganga) | 1.64 | 🟡 Alert | 0.000 |  |
| 2026-10-31 13:02:17 | Pitabeddara (Nilwala Ganga) | 1.46 | 🟢 Normal | -0.011 |  |
| 2026-10-31 13:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.90 | 🟢 Normal | -0.113 |  |
| 2026-10-31 13:02:08 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-10-31 13:02:00 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.083 |  |
| 2026-10-31 13:01:53 | Putupaula (Kalu Ganga) | 2.21 | 🟢 Normal | -0.051 |  |
| 2026-10-31 13:01:49 | Horowpothana (Yan Oya) | 2.24 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-31 13:01:48 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-10-31 13:01:41 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 13:01:37 | Panadugama (Nilwala Ganga) | 4.69 | 🟢 Normal | -0.032 |  |
| 2026-10-31 13:01:30 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-10-31 13:01:27 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-31 13:01:05 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.020 |  |
| 2026-10-31 13:00:26 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-10-31 13:00:10 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.052 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 13:02:29 | Thalgahagoda (Nilwala Ganga) | 1.64 | 🟡 Alert | 0.000 |  |
| 2026-10-31 13:01:49 | Horowpothana (Yan Oya) | 2.24 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-31 12:03:30 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-31 13:00:26 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-10-31 12:01:59 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-31 13:01:41 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 12:03:01 | Galgamuwa (Mee Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-31 13:03:13 | Glencourse (Kelani Ganga) | 10.63 | 🟢 Normal | 0.000 |  |
| 2026-10-31 12:04:24 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-31 13:02:46 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-31 13:01:48 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-10-31 12:03:55 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-31 13:01:27 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-31 13:02:48 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-10-31 12:06:25 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-31 12:01:17 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-10-31 12:01:20 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-31 13:02:17 | Pitabeddara (Nilwala Ganga) | 1.46 | 🟢 Normal | -0.011 |  |
| 2026-10-31 12:00:56 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.011 |  |
| 2026-10-31 13:02:39 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.020 |  |
| 2026-10-31 12:01:36 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-10-31 12:03:11 | Hanwella (Kelani Ganga) | 2.62 | 🟢 Normal | -0.020 |  |
| 2026-10-31 13:01:05 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.020 |  |
| 2026-10-31 12:01:10 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.021 |  |
| 2026-10-31 12:06:29 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | -0.029 |  |
| 2026-10-31 13:02:08 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-10-31 13:01:30 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-10-31 12:03:11 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | -0.030 |  |
| 2026-10-31 13:03:14 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.031 |  |
| 2026-10-31 12:03:23 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | -0.031 |  |
| 2026-10-31 13:01:37 | Panadugama (Nilwala Ganga) | 4.69 | 🟢 Normal | -0.032 |  |
| 2026-10-31 12:11:26 | Baddegama (Gin Ganga) | 2.55 | 🟢 Normal | -0.044 |  |
| 2026-10-31 13:01:53 | Putupaula (Kalu Ganga) | 2.21 | 🟢 Normal | -0.051 |  |
| 2026-10-31 13:00:10 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.052 |  |
| 2026-10-31 13:03:06 | Ellagawa (Kalu Ganga) | 6.58 | 🟢 Normal | -0.064 |  |
| 2026-10-31 12:04:47 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.066 |  |
| 2026-10-31 13:02:38 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.071 |  |
| 2026-10-31 13:02:00 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.083 |  |
| 2026-10-31 13:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.90 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)