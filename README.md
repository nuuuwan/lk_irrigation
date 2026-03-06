# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--06_09:23:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **90,611 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-06 09:23:42 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:12:58 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:09:06 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:09:06 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-06 09:07:18 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:06:54 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-03-06 09:06:44 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-06 09:06:03 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:05:54 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:05:51 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:05:29 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | -0.019 |  |
| 2026-03-06 09:05:18 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.019 |  |
| 2026-03-06 09:05:03 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.047 |  |
| 2026-03-06 09:03:48 | Putupaula (Kalu Ganga) | 0.25 | 🟢 Normal | -0.119 |  |
| 2026-03-06 09:03:44 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:03:34 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-06 09:03:27 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:03:23 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-03-06 09:03:18 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:03:12 | Thawalama (Gin Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:02:56 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | -0.060 |  |
| 2026-03-06 09:02:35 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 09:02:31 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-03-06 09:02:25 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | -0.017 |  |
| 2026-03-06 09:02:23 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:02:21 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.074 |  |
| 2026-03-06 09:02:09 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:02:05 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:02:05 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:02:01 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:01:53 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 1.500 | 🔺 Rising |
| 2026-03-06 09:01:31 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:01:29 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 1.500 | 🔺 Rising |
| 2026-03-06 09:01:13 | Kithulgala (Kelani Ganga) | 1.38 | 🟢 Normal | -0.170 |  |
| 2026-03-06 09:01:10 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-03-06 09:00:55 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:00:55 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:00:55 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-06 09:01:53 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 1.500 | 🔺 Rising |
| 2026-03-06 09:03:23 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-03-06 09:09:06 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-06 09:06:44 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-06 09:03:34 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-06 09:02:35 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 09:12:58 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:02:01 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:01:10 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:02:23 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:01:31 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:07:18 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:09:06 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:02:05 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:02:09 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:02:56 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-03-06 08:18:07 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:06:03 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:03:27 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:00:55 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:00:55 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:05:51 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:02:05 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:05:54 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:03:44 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:00:55 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:03:12 | Thawalama (Gin Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:23:42 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-06 09:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-03-06 09:06:54 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-03-06 09:02:31 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-03-06 09:02:25 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | -0.017 |  |
| 2026-03-06 09:05:18 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.019 |  |
| 2026-03-06 09:05:29 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | -0.019 |  |
| 2026-03-06 09:05:03 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.047 |  |
| 2026-03-06 09:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | -0.060 |  |
| 2026-03-06 09:02:21 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.074 |  |
| 2026-03-06 09:03:48 | Putupaula (Kalu Ganga) | 0.25 | 🟢 Normal | -0.119 |  |
| 2026-03-06 09:01:13 | Kithulgala (Kelani Ganga) | 1.38 | 🟢 Normal | -0.170 |  |

## River Water Level Charts by Station

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)