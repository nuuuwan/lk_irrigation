# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_00:14:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **121,701 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 00:14:27 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.021 |  |
| 2026-04-11 00:12:51 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.023 |  |
| 2026-04-11 00:10:11 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:09:22 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-04-11 00:08:06 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-11 00:08:04 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:06:57 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:06:04 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:05:37 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.063 |  |
| 2026-04-11 00:05:28 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-04-11 00:05:05 | Peradeniya (Mahaweli Ganga) | 1.89 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-04-11 00:04:27 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 00:03:29 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:03:17 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:03:14 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | -0.011 |  |
| 2026-04-11 00:03:08 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:02:52 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:02:48 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:02:21 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:02:21 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-04-11 00:02:19 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.021 |  |
| 2026-04-11 00:02:07 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-04-11 00:02:02 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.069 |  |
| 2026-04-11 00:01:57 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.021 |  |
| 2026-04-11 00:01:42 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:01:40 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:01:10 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:01:09 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:01:01 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-10 23:48:26 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.025 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 18:06:03 | Weraganthota (Mahaweli Ganga) | -2.20 | 🟢 Normal | 0.886 | 🔺 Rising |
| 2026-04-11 00:05:05 | Peradeniya (Mahaweli Ganga) | 1.89 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-04-10 22:14:50 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-10 23:06:31 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-04-10 23:39:42 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-11 00:08:06 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-10 22:01:52 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 23:00:48 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 00:04:27 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 00:06:57 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:01:09 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:02:48 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:03:08 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:01:42 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:02:21 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-10 18:02:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:03:17 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:08:04 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:03:29 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:01:40 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:01:01 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-10 23:02:28 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:02:52 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:10:11 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 00:06:04 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 21:39:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.18 | 🟢 Normal | -0.008 |  |
| 2026-04-11 00:09:22 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-04-10 18:01:05 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-04-11 00:02:21 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-04-11 00:02:07 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-04-11 00:03:14 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | -0.011 |  |
| 2026-04-11 00:05:28 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-04-11 00:02:19 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.021 |  |
| 2026-04-11 00:14:27 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.021 |  |
| 2026-04-11 00:01:57 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.021 |  |
| 2026-04-11 00:12:51 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.023 |  |
| 2026-04-10 23:48:26 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.025 |  |
| 2026-04-11 00:05:37 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.063 |  |
| 2026-04-11 00:02:02 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)