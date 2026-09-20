# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_06:12:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **265,794 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Nawalapitiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 06:12:43 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-09-20 06:10:22 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-09-20 06:10:09 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-20 06:09:50 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-09-20 06:07:42 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-20 06:07:34 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-20 06:07:34 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-20 06:07:15 | Rathnapura (Kalu Ganga) | 1.96 | 🟢 Normal | 0.326 | 🔺 Rising |
| 2026-09-20 06:07:08 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-20 06:07:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.56 | 🟢 Normal | 0.259 | 🔺 Rising |
| 2026-09-20 06:06:27 | Deraniyagala (Kelani Ganga) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-09-20 06:06:18 | Kithulgala (Kelani Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-09-20 06:06:05 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-09-20 06:05:12 | Nawalapitiya (Mahaweli Ganga) | 3.57 | 🟡 Alert | -0.031 |  |
| 2026-09-20 06:05:10 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 06:05:09 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-09-20 06:04:35 | Ellagawa (Kalu Ganga) | 5.69 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-09-20 06:04:22 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-09-20 06:03:59 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-20 06:03:40 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-20 06:03:39 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-20 06:03:35 | Hanwella (Kelani Ganga) | 1.90 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-20 06:03:28 | Glencourse (Kelani Ganga) | 10.39 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-09-20 06:03:20 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-20 06:03:20 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 06:03:09 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-20 06:02:34 | Magura (Kalu Ganga) | 4.20 | 🟡 Alert | 0.097 | 🔺 Rising |
| 2026-09-20 06:02:19 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-20 06:02:09 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-20 06:02:00 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | 0.004 |  |
| 2026-09-20 06:01:53 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-09-20 06:01:51 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 06:01:36 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-09-20 06:01:36 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.005 |  |
| 2026-09-20 06:01:30 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 06:01:09 | Thawalama (Gin Ganga) | 2.84 | 🟢 Normal | 0.547 | 🔺 Rising |
| 2026-09-20 06:01:05 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:55:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.51 | 🟢 Normal | 0.259 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 06:02:34 | Magura (Kalu Ganga) | 4.20 | 🟡 Alert | 0.097 | 🔺 Rising |
| 2026-09-20 06:05:12 | Nawalapitiya (Mahaweli Ganga) | 3.57 | 🟡 Alert | -0.031 |  |
| 2026-09-20 06:01:09 | Thawalama (Gin Ganga) | 2.84 | 🟢 Normal | 0.547 | 🔺 Rising |
| 2026-09-20 06:07:15 | Rathnapura (Kalu Ganga) | 1.96 | 🟢 Normal | 0.326 | 🔺 Rising |
| 2026-09-20 06:07:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.56 | 🟢 Normal | 0.259 | 🔺 Rising |
| 2026-09-20 06:04:22 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-09-20 06:04:35 | Ellagawa (Kalu Ganga) | 5.69 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-09-20 06:10:22 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-09-20 06:09:50 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-09-20 06:03:20 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-20 06:05:09 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-09-20 06:03:35 | Hanwella (Kelani Ganga) | 1.90 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-20 06:12:43 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-09-20 06:03:40 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-20 06:03:28 | Glencourse (Kelani Ganga) | 10.39 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-09-20 06:07:34 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-20 06:07:42 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-20 06:01:51 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 06:06:05 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-09-20 06:07:34 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-20 06:02:00 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | 0.004 |  |
| 2026-09-20 06:06:18 | Kithulgala (Kelani Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-09-20 06:02:19 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-20 06:03:39 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-20 06:03:59 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-20 06:01:30 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 06:03:09 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-20 06:07:08 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-19 18:01:55 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-20 06:05:10 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 06:10:09 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-20 06:03:20 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 06:02:09 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-20 06:01:05 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-19 18:01:39 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-20 06:01:36 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.005 |  |
| 2026-09-20 06:06:27 | Deraniyagala (Kelani Ganga) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-09-20 06:01:53 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-09-20 06:01:36 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.021 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)