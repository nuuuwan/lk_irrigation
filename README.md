# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--29_09:13:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **192,412 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 09:13:16 | Ellagawa (Kalu Ganga) | 5.53 | 🟢 Normal | 0.000 |  |
| 2026-06-29 09:13:15 | Ellagawa (Kalu Ganga) | 5.53 | 🟢 Normal | 0.000 |  |
| 2026-06-29 09:10:58 | Panadugama (Nilwala Ganga) | 3.59 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-06-29 09:10:41 | Rathnapura (Kalu Ganga) | 2.40 | 🟢 Normal | 0.364 | 🔺 Rising |
| 2026-06-29 09:09:59 | Thawalama (Gin Ganga) | 2.89 | 🟢 Normal | 0.318 | 🔺 Rising |
| 2026-06-29 09:09:51 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-29 09:09:24 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-29 09:07:44 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-29 09:06:30 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-06-29 09:06:29 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-29 09:06:17 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-29 09:05:39 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-29 09:05:39 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-29 09:05:31 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-06-29 09:05:00 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-29 09:04:15 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-29 09:04:12 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-29 09:03:44 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-06-29 09:03:36 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 09:03:14 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.012 |  |
| 2026-06-29 09:03:12 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 09:03:08 | Thanthirimale (Malwathu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-06-29 09:02:58 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-29 09:02:58 | Nawalapitiya (Mahaweli Ganga) | 1.94 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-06-29 09:02:56 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-29 09:02:41 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-29 09:02:30 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.021 |  |
| 2026-06-29 09:02:29 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-29 09:02:09 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-06-29 09:02:06 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-29 09:01:52 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 09:01:51 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 09:01:47 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-06-29 09:01:20 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 09:01:13 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.010 |  |
| 2026-06-29 09:01:05 | Moragaswewa (Deduru Oya) | 0.12 | 🟢 Normal | -0.011 |  |
| 2026-06-29 09:00:52 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 09:00:52 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 09:10:41 | Rathnapura (Kalu Ganga) | 2.40 | 🟢 Normal | 0.364 | 🔺 Rising |
| 2026-06-29 09:09:59 | Thawalama (Gin Ganga) | 2.89 | 🟢 Normal | 0.318 | 🔺 Rising |
| 2026-06-29 08:08:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.14 | 🟢 Normal | 0.298 | 🔺 Rising |
| 2026-06-29 09:01:47 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-06-29 09:10:58 | Panadugama (Nilwala Ganga) | 3.59 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-06-29 09:02:58 | Nawalapitiya (Mahaweli Ganga) | 1.94 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-06-29 09:03:44 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-06-29 09:07:44 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-29 09:02:06 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-29 09:09:51 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-29 09:06:29 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-29 09:02:29 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-29 09:02:56 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-29 09:05:39 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-29 09:04:15 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-29 09:02:58 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-29 09:05:39 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-29 09:03:12 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 09:03:36 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 09:01:20 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 09:01:52 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 09:09:24 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-29 09:05:31 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-06-29 09:00:52 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 09:01:51 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 09:05:00 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-29 09:13:16 | Ellagawa (Kalu Ganga) | 5.53 | 🟢 Normal | 0.000 |  |
| 2026-06-29 09:06:17 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-29 09:00:52 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 08:02:15 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 09:06:30 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-06-29 09:03:08 | Thanthirimale (Malwathu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-06-29 09:04:12 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-29 09:02:41 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-29 09:01:13 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.010 |  |
| 2026-06-29 09:02:09 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-06-29 09:01:05 | Moragaswewa (Deduru Oya) | 0.12 | 🟢 Normal | -0.011 |  |
| 2026-06-29 09:03:14 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.012 |  |
| 2026-06-29 09:02:30 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.021 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)