# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--14_21:09:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **73,162 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 21:09:27 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:08:32 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-02-14 21:06:43 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.038 |  |
| 2026-02-14 21:05:35 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.005 |  |
| 2026-02-14 21:05:32 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:05:16 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:05:11 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:04:46 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.066 |  |
| 2026-02-14 21:04:10 | Padiyathalawa (Maduru Oya) | 1.80 | 🟢 Normal | -0.100 |  |
| 2026-02-14 21:03:48 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.019 |  |
| 2026-02-14 21:03:31 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-14 21:03:28 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-02-14 21:03:14 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.031 |  |
| 2026-02-14 21:03:13 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:02:59 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:02:37 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:02:35 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | 0.404 | 🔺 Rising |
| 2026-02-14 21:02:31 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:02:26 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.030 |  |
| 2026-02-14 21:02:19 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:02:15 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:02:13 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-02-14 21:02:01 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-14 21:01:56 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:01:43 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:01:40 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:01:02 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:00:46 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 21:00:41 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-14 21:00:32 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:46:51 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:31:45 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:21:48 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 21:02:35 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | 0.404 | 🔺 Rising |
| 2026-02-14 20:09:34 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-02-14 21:02:01 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-14 21:03:31 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-14 21:00:46 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 18:02:04 | Weraganthota (Mahaweli Ganga) | -1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 20:06:52 | Glencourse (Kelani Ganga) | 8.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 21:03:13 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:02:59 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:05:16 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:05:32 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:01:43 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:01:40 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:00:32 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:03:27 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:02:19 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:09:34 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:02:37 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:01:56 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:05:05 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:05:11 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:09:27 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:02:15 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:01:28 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:46:51 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:02:31 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:04:52 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:09:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-02-14 21:05:35 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.005 |  |
| 2026-02-14 21:03:28 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-02-14 21:00:41 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-14 21:02:13 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-02-14 21:08:32 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-02-14 21:03:48 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.019 |  |
| 2026-02-14 21:02:26 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.030 |  |
| 2026-02-14 21:03:14 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.031 |  |
| 2026-02-14 21:06:43 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.038 |  |
| 2026-02-14 21:04:46 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.066 |  |
| 2026-02-14 21:04:10 | Padiyathalawa (Maduru Oya) | 1.80 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)