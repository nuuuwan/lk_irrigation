# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--19_16:08:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **292,306 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 16:08:34 | Rathnapura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.036 |  |
| 2026-10-19 16:08:33 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | -0.019 |  |
| 2026-10-19 16:06:40 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-10-19 16:06:35 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-10-19 16:06:20 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-10-19 16:06:09 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.020 |  |
| 2026-10-19 16:05:44 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-19 16:05:41 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-19 16:05:22 | Glencourse (Kelani Ganga) | 10.96 | 🟢 Normal | -0.039 |  |
| 2026-10-19 16:05:14 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | -0.010 |  |
| 2026-10-19 16:05:12 | Panadugama (Nilwala Ganga) | 5.18 | 🟡 Alert | -0.029 |  |
| 2026-10-19 16:05:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.65 | 🟢 Normal | -0.039 |  |
| 2026-10-19 16:03:52 | Pitabeddara (Nilwala Ganga) | 1.64 | 🟢 Normal | -0.068 |  |
| 2026-10-19 16:03:52 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 16:03:48 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-10-19 16:03:26 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-19 16:03:22 | Thalgahagoda (Nilwala Ganga) | 1.89 | 🟠 Minor Flood | -0.011 |  |
| 2026-10-19 16:03:11 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-10-19 16:03:11 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 16:02:57 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-10-19 16:02:52 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-10-19 16:02:39 | Hanwella (Kelani Ganga) | 2.99 | 🟢 Normal | -0.080 |  |
| 2026-10-19 16:02:38 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-19 16:02:29 | Ellagawa (Kalu Ganga) | 6.90 | 🟢 Normal | -0.052 |  |
| 2026-10-19 16:01:52 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-10-19 16:01:45 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 16:01:33 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-19 16:01:24 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.053 |  |
| 2026-10-19 16:01:23 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-10-19 16:01:14 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | -0.051 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 16:03:22 | Thalgahagoda (Nilwala Ganga) | 1.89 | 🟠 Minor Flood | -0.011 |  |
| 2026-10-19 16:05:12 | Panadugama (Nilwala Ganga) | 5.18 | 🟡 Alert | -0.029 |  |
| 2026-10-19 16:06:35 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-10-19 16:03:52 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 16:03:11 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 16:01:45 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 16:05:44 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-19 15:02:12 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-10-19 16:03:26 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-19 15:05:25 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-19 16:01:33 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-19 16:05:41 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-19 16:01:23 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-10-19 15:17:15 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.009 |  |
| 2026-10-19 16:06:20 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-10-19 16:05:14 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | -0.010 |  |
| 2026-10-19 16:02:38 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-19 16:06:40 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-10-19 15:00:52 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-10-19 16:03:48 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-10-19 16:01:52 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-10-19 16:03:11 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-10-19 16:02:52 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-10-19 15:04:40 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.012 |  |
| 2026-10-19 16:08:33 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | -0.019 |  |
| 2026-10-19 16:06:09 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.020 |  |
| 2026-10-19 16:02:57 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-10-19 15:03:34 | Moragaswewa (Deduru Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-10-19 15:10:10 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | -0.033 |  |
| 2026-10-19 16:08:34 | Rathnapura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.036 |  |
| 2026-10-19 16:05:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.65 | 🟢 Normal | -0.039 |  |
| 2026-10-19 16:05:22 | Glencourse (Kelani Ganga) | 10.96 | 🟢 Normal | -0.039 |  |
| 2026-10-19 16:01:14 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | -0.051 |  |
| 2026-10-19 16:02:29 | Ellagawa (Kalu Ganga) | 6.90 | 🟢 Normal | -0.052 |  |
| 2026-10-19 16:01:24 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.053 |  |
| 2026-10-19 16:03:52 | Pitabeddara (Nilwala Ganga) | 1.64 | 🟢 Normal | -0.068 |  |
| 2026-10-19 16:02:39 | Hanwella (Kelani Ganga) | 2.99 | 🟢 Normal | -0.080 |  |
| 2026-10-19 15:04:30 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.083 |  |
| 2026-10-19 15:05:17 | Galgamuwa (Mee Oya) | 0.69 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)