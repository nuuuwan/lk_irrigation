# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--19_10:18:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **77,187 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 10:18:39 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.016 |  |
| 2026-02-19 10:14:59 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.009 |  |
| 2026-02-19 10:12:25 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:12:19 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.018 |  |
| 2026-02-19 10:11:26 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:07:03 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.034 |  |
| 2026-02-19 10:05:58 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:05:55 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:05:42 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:05:20 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 10:05:14 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:05:10 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:04:22 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.019 |  |
| 2026-02-19 10:04:20 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:03:54 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:03:43 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:03:31 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-19 10:03:19 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-19 10:03:13 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:03:08 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:03:07 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.020 |  |
| 2026-02-19 10:03:01 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:02:52 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 10:02:38 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | -0.019 |  |
| 2026-02-19 10:02:18 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:02:12 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-19 10:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.040 |  |
| 2026-02-19 10:02:09 | Manampitiya (Mahaweli Ganga) | 2.31 | 🟢 Normal | -0.040 |  |
| 2026-02-19 10:02:08 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:02:05 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.305 |  |
| 2026-02-19 10:01:59 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:01:59 | Weraganthota (Mahaweli Ganga) | -1.78 | 🟢 Normal | 0.337 | 🔺 Rising |
| 2026-02-19 10:01:55 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:01:53 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-02-19 10:01:48 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:01:39 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:01:39 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:01:32 | Putupaula (Kalu Ganga) | 0.15 | 🟢 Normal | -0.093 |  |
| 2026-02-19 10:01:02 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 10:01:59 | Weraganthota (Mahaweli Ganga) | -1.78 | 🟢 Normal | 0.337 | 🔺 Rising |
| 2026-02-19 10:02:12 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-19 10:03:19 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-19 10:03:31 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-19 10:02:52 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 10:05:20 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 10:02:18 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:01:39 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:03:43 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:01:48 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:03:13 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:05:42 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:01:02 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:01:55 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:05:55 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:03:08 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:11:26 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:05:10 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:05:14 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:02:08 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:04:20 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:03:01 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:01:39 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:05:58 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:01:59 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:03:54 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:12:25 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-19 10:14:59 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.009 |  |
| 2026-02-19 10:01:53 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-02-19 10:18:39 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.016 |  |
| 2026-02-19 10:12:19 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.018 |  |
| 2026-02-19 10:04:22 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.019 |  |
| 2026-02-19 10:02:38 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | -0.019 |  |
| 2026-02-19 10:03:07 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.020 |  |
| 2026-02-19 10:07:03 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.034 |  |
| 2026-02-19 10:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.040 |  |
| 2026-02-19 10:02:09 | Manampitiya (Mahaweli Ganga) | 2.31 | 🟢 Normal | -0.040 |  |
| 2026-02-19 10:01:32 | Putupaula (Kalu Ganga) | 0.15 | 🟢 Normal | -0.093 |  |
| 2026-02-19 10:02:05 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.305 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)