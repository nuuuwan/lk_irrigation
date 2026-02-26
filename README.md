# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--26_14:10:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **83,625 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 14:10:54 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:08:33 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:07:10 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 14:06:04 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:04:55 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | -0.013 |  |
| 2026-02-26 14:04:39 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:04:28 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:04:21 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:04:14 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-26 14:04:10 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:04:10 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.069 |  |
| 2026-02-26 14:04:04 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:04:01 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-26 14:03:52 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:03:21 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:03:21 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:03:18 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-02-26 14:03:17 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:03:15 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:02:56 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-26 14:02:53 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:02:39 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-02-26 14:02:38 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:02:34 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:02:33 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | -0.070 |  |
| 2026-02-26 14:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 14:02:16 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 14:02:11 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:02:07 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:02:05 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-26 14:02:01 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:01:52 | Weraganthota (Mahaweli Ganga) | -1.66 | 🟢 Normal | -0.019 |  |
| 2026-02-26 14:01:44 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-02-26 14:01:23 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:01:23 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:01:18 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:01:14 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:01:11 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-26 13:21:26 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 14:04:14 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-26 13:03:47 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-26 14:02:56 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-26 14:04:01 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-26 14:02:05 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-26 14:02:16 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 14:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 14:07:10 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 14:01:23 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:01:23 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:02:01 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:10:54 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:08:33 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:03:21 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:04:21 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:02:38 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:03:21 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:04:39 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:04:04 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:03:52 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:04:28 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:01:14 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:01:18 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:02:34 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:02:53 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:03:17 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:06:04 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:04:10 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:01:11 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:02:07 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:03:15 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:02:11 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-26 14:01:44 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-02-26 14:03:18 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-02-26 14:02:39 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-02-26 14:04:55 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | -0.013 |  |
| 2026-02-26 14:01:52 | Weraganthota (Mahaweli Ganga) | -1.66 | 🟢 Normal | -0.019 |  |
| 2026-02-26 14:04:10 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.069 |  |
| 2026-02-26 14:02:33 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)