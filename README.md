# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--18_20:15:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **76,690 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-18 20:15:22 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:13:44 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.834 |  |
| 2026-02-18 20:13:41 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:12:28 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:11:30 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:10:46 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:07:59 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.087 |  |
| 2026-02-18 20:07:53 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-18 20:06:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.153 |  |
| 2026-02-18 20:05:44 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:05:01 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:04:52 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:04:34 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-02-18 20:04:31 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 20:04:16 | Manampitiya (Mahaweli Ganga) | 3.05 | 🟡 Alert | 0.000 |  |
| 2026-02-18 20:04:08 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:04:02 | Dunamale (Aththanagalu Oya) | 0.10 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-18 20:03:51 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:03:47 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.031 |  |
| 2026-02-18 20:03:40 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-02-18 20:03:32 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:03:31 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:03:30 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:03:17 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-02-18 20:03:16 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:03:04 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.049 |  |
| 2026-02-18 20:02:43 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 20:02:39 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:02:37 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:02:36 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:02:25 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-02-18 20:02:24 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:02:13 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-18 20:02:07 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-02-18 20:01:35 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-02-18 20:00:50 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.021 |  |
| 2026-02-18 20:00:27 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.063 |  |
| 2026-02-18 19:50:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.153 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-18 20:04:16 | Manampitiya (Mahaweli Ganga) | 3.05 | 🟡 Alert | 0.000 |  |
| 2026-02-18 20:02:07 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-02-18 20:02:13 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-18 20:04:02 | Dunamale (Aththanagalu Oya) | 0.10 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-18 20:07:53 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-18 20:03:40 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-02-18 20:04:31 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 20:02:43 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 20:02:37 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:12:28 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:02:39 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:13:41 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:02:24 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-18 18:04:47 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:11:30 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:03:31 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:03:32 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:04:52 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-18 19:05:51 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:03:16 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:05:01 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:04:08 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:10:46 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-18 18:01:21 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:05:44 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:15:22 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:02:36 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-18 20:03:17 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-02-18 20:04:34 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-02-18 18:01:50 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | -0.010 |  |
| 2026-02-18 20:02:25 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-02-18 20:01:35 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-02-18 20:00:50 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.021 |  |
| 2026-02-18 20:03:47 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.031 |  |
| 2026-02-18 20:03:04 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.049 |  |
| 2026-02-18 20:00:27 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.063 |  |
| 2026-02-18 20:07:59 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.087 |  |
| 2026-02-18 20:06:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.153 |  |
| 2026-02-18 20:13:44 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.834 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)