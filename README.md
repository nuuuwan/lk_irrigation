# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--13_21:35:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **72,270 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 21:35:55 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:35:39 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:12:45 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:11:25 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:07:43 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:07:15 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-13 21:07:06 | Manampitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-02-13 21:05:54 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:05:44 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.019 |  |
| 2026-02-13 21:05:41 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:05:04 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-13 21:04:46 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:04:41 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-02-13 21:04:04 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:03:55 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:03:40 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:03:39 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:03:13 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 21:03:00 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:02:50 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:02:45 | Glencourse (Kelani Ganga) | 8.22 | 🟢 Normal | -0.042 |  |
| 2026-02-13 21:02:44 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:02:44 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:02:44 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:02:31 | Ellagawa (Kalu Ganga) | 4.44 | 🟢 Normal | -0.011 |  |
| 2026-02-13 21:02:27 | Padiyathalawa (Maduru Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-02-13 21:02:24 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-02-13 21:02:11 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-02-13 21:02:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-02-13 21:01:59 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-02-13 21:01:52 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-02-13 21:01:48 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:01:38 | Peradeniya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.372 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 21:01:38 | Peradeniya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.372 | 🔺 Rising |
| 2026-02-13 21:07:06 | Manampitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-02-13 21:02:24 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-02-13 21:01:35 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-02-13 21:07:15 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-13 21:03:13 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 21:02:50 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:02:44 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:07:43 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:01:48 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:02:44 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:00:50 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:11:25 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:03:39 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:35:55 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:12:45 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:03:00 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:04:04 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:05:41 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:04:46 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:03:07 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:35:39 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:03:40 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:03:55 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:05:54 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-13 21:04:41 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-02-13 21:02:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-02-13 21:02:11 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-02-13 21:02:27 | Padiyathalawa (Maduru Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-02-13 21:01:59 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-02-13 21:05:04 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-13 21:02:31 | Ellagawa (Kalu Ganga) | 4.44 | 🟢 Normal | -0.011 |  |
| 2026-02-13 21:01:52 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-02-13 21:05:44 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.019 |  |
| 2026-02-13 21:01:15 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.022 |  |
| 2026-02-13 20:16:05 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.026 |  |
| 2026-02-13 21:02:45 | Glencourse (Kelani Ganga) | 8.22 | 🟢 Normal | -0.042 |  |
| 2026-02-13 18:01:13 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | -0.050 |  |
| 2026-02-13 21:01:10 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)