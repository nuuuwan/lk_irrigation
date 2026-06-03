# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--04_00:11:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **169,749 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 00:11:48 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.027 |  |
| 2026-06-04 00:11:18 | Ellagawa (Kalu Ganga) | 5.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-04 00:08:07 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 00:07:46 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-04 00:07:08 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-06-04 00:07:07 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-06-04 00:06:48 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.019 |  |
| 2026-06-04 00:06:47 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-04 00:06:02 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.065 |  |
| 2026-06-04 00:05:56 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-04 00:05:49 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.011 |  |
| 2026-06-04 00:05:09 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 00:04:59 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-04 00:04:42 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-06-04 00:04:40 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-06-04 00:04:17 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-06-04 00:03:59 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.244 | 🔺 Rising |
| 2026-06-04 00:03:57 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-04 00:03:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-04 00:03:41 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.214 |  |
| 2026-06-04 00:03:40 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 00:03:39 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-04 00:03:34 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-04 00:03:17 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-04 00:02:49 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-06-04 00:02:43 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-06-04 00:02:39 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 00:02:18 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 00:02:16 | Moragaswewa (Deduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-04 00:02:07 | Dunamale (Aththanagalu Oya) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 00:02:05 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-04 00:02:03 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-04 00:02:02 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.021 |  |
| 2026-06-04 00:01:47 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-04 00:01:26 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 00:00:55 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 00:04:42 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-06-04 00:03:59 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.244 | 🔺 Rising |
| 2026-06-04 00:02:49 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-06-04 00:01:47 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-04 00:04:17 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-06-04 00:04:59 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-04 00:03:17 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-04 00:03:57 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-04 00:03:39 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-04 00:03:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-04 00:02:03 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-04 00:02:07 | Dunamale (Aththanagalu Oya) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 00:05:09 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 00:03:40 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 00:05:56 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-04 00:11:18 | Ellagawa (Kalu Ganga) | 5.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-03 18:00:51 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-06-04 00:00:55 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 00:02:16 | Moragaswewa (Deduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-04 00:01:26 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 00:02:05 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:03:16 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-04 00:08:07 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 00:02:18 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-04 00:03:34 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:08:36 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-03 23:03:32 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-04 00:07:46 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-04 00:02:43 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-06-03 18:01:27 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-04 00:07:08 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-06-04 00:06:47 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-03 22:00:14 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-06-04 00:05:49 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.011 |  |
| 2026-06-04 00:06:48 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.019 |  |
| 2026-06-04 00:02:02 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.021 |  |
| 2026-06-04 00:11:48 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.027 |  |
| 2026-06-04 00:06:02 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.065 |  |
| 2026-06-04 00:03:41 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.214 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)