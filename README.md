# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--29_10:20:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **192,454 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 10:20:36 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-06-29 10:13:04 | Pitabeddara (Nilwala Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-29 10:12:20 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-06-29 10:10:39 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-06-29 10:10:36 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-29 10:09:16 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-29 10:09:12 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-29 10:08:10 | Ellagawa (Kalu Ganga) | 5.67 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-06-29 10:07:47 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-06-29 10:07:23 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-29 10:06:51 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-06-29 10:06:31 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 10:06:27 | Panadugama (Nilwala Ganga) | 3.89 | 🟢 Normal | 0.324 | 🔺 Rising |
| 2026-06-29 10:06:10 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-29 10:06:08 | Thawalama (Gin Ganga) | 2.99 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-06-29 10:04:57 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-29 10:03:47 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-06-29 10:03:41 | Rathnapura (Kalu Ganga) | 2.97 | 🟢 Normal | 0.645 | 🔺 Rising |
| 2026-06-29 10:03:30 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-29 10:03:27 | Deraniyagala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.509 | 🔺 Rising |
| 2026-06-29 10:03:21 | Pitabeddara (Nilwala Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-29 10:03:07 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-29 10:03:05 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-06-29 10:03:03 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 10:02:41 | Magura (Kalu Ganga) | 2.68 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-06-29 10:02:37 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 10:02:30 | Nawalapitiya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.443 | 🔺 Rising |
| 2026-06-29 10:02:26 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 10:02:18 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-29 10:02:09 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-29 10:02:09 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-29 10:02:05 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-29 10:02:03 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-29 10:01:44 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.030 |  |
| 2026-06-29 10:01:39 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-06-29 10:01:37 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 10:00:51 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-29 10:00:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.26 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-29 10:00:39 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-29 10:00:35 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 10:03:41 | Rathnapura (Kalu Ganga) | 2.97 | 🟢 Normal | 0.645 | 🔺 Rising |
| 2026-06-29 10:03:27 | Deraniyagala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.509 | 🔺 Rising |
| 2026-06-29 10:02:30 | Nawalapitiya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.443 | 🔺 Rising |
| 2026-06-29 10:06:27 | Panadugama (Nilwala Ganga) | 3.89 | 🟢 Normal | 0.324 | 🔺 Rising |
| 2026-06-29 10:02:41 | Magura (Kalu Ganga) | 2.68 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-06-29 10:03:05 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-06-29 10:08:10 | Ellagawa (Kalu Ganga) | 5.67 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-06-29 10:12:20 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-06-29 10:06:08 | Thawalama (Gin Ganga) | 2.99 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-06-29 10:06:51 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-06-29 10:03:47 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-06-29 10:20:36 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-06-29 10:07:47 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-06-29 10:00:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.26 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-29 10:02:09 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-29 10:09:16 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-29 10:04:57 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-29 10:00:39 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-29 09:02:58 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-29 10:02:03 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-29 10:03:03 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 10:06:31 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 10:10:36 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-29 10:03:07 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-29 10:02:37 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 10:07:23 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-29 10:01:37 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 10:00:51 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-29 10:02:18 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-29 10:13:04 | Pitabeddara (Nilwala Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-29 10:03:30 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-29 10:02:26 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 10:09:12 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-29 10:02:05 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-29 10:02:09 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-29 10:10:39 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-06-29 10:00:35 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-06-29 10:01:39 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-06-29 10:01:44 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.030 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)