# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_11:10:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **111,391 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 11:10:33 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:09:09 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.046 |  |
| 2026-03-30 11:09:06 | Badalgama (Maha Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:08:38 | Ellagawa (Kalu Ganga) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:07:58 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.336 | 🔺 Rising |
| 2026-03-30 11:07:22 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | -0.058 |  |
| 2026-03-30 11:06:59 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:06:36 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:06:35 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-03-30 11:06:20 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-30 11:06:06 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.019 |  |
| 2026-03-30 11:06:05 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-03-30 11:06:01 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-03-30 11:05:35 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.032 |  |
| 2026-03-30 11:04:51 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:04:17 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-03-30 11:03:43 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:03:43 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-03-30 11:03:41 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-03-30 11:03:33 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:03:26 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-30 11:03:04 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-03-30 11:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-03-30 11:02:56 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:02:41 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:02:29 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-30 11:02:09 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.023 |  |
| 2026-03-30 11:02:09 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:02:07 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 11:02:03 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:01:59 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:01:39 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:01:33 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:01:25 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | -0.191 |  |
| 2026-03-30 11:01:01 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 11:00:35 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-03-30 11:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-03-30 10:25:11 | Ellagawa (Kalu Ganga) | 3.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 11:07:58 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.336 | 🔺 Rising |
| 2026-03-30 11:06:05 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-03-30 11:03:04 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-03-30 11:06:01 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-03-30 11:03:41 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-03-30 11:06:20 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-30 11:03:26 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-30 11:02:29 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-30 11:01:01 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 11:02:07 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 11:02:03 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:01:39 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:06:59 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:01:33 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:01:59 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-30 10:00:39 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:06:36 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:02:56 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:08:38 | Ellagawa (Kalu Ganga) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:03:33 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-03-30 10:00:48 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:02:41 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:09:06 | Badalgama (Maha Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:04:51 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:10:33 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:03:43 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:02:09 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 11:06:35 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-03-30 11:04:17 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-03-30 11:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-03-30 11:00:35 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-03-30 11:06:06 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.019 |  |
| 2026-03-30 11:03:43 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-03-30 11:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-03-30 11:02:09 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.023 |  |
| 2026-03-30 11:05:35 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.032 |  |
| 2026-03-30 11:09:09 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.046 |  |
| 2026-03-30 11:07:22 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | -0.058 |  |
| 2026-03-30 11:01:25 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | -0.191 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)