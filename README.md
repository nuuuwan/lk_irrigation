# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--24_13:04:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **81,789 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 13:04:48 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-24 13:04:25 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-02-24 13:04:12 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-02-24 13:04:05 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-24 13:03:58 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-24 13:03:31 | Nagalagam Street (Kelani Ganga) | 0.26 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-02-24 13:03:23 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-24 13:03:19 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-24 13:03:04 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.021 |  |
| 2026-02-24 13:02:57 | Putupaula (Kalu Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 13:02:54 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-02-24 13:02:48 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-24 13:02:38 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-24 13:02:37 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -0.020 |  |
| 2026-02-24 13:02:34 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-24 13:02:33 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-24 13:01:58 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-02-24 13:01:53 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-24 13:01:20 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-02-24 13:01:18 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 13:01:15 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-24 13:01:03 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-02-24 13:00:19 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 12:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-24 13:03:31 | Nagalagam Street (Kelani Ganga) | 0.26 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-02-24 13:01:15 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-24 12:02:38 | Manampitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-24 12:00:53 | Weraganthota (Mahaweli Ganga) | -1.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-24 13:02:57 | Putupaula (Kalu Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 13:01:20 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-02-24 13:01:18 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 12:02:05 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 13:01:53 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-24 13:03:19 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-24 13:02:38 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-24 12:02:36 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-24 12:04:41 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-24 12:01:43 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-24 13:03:23 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-24 13:04:05 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-24 12:06:02 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-02-24 13:02:33 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-24 13:02:48 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-24 12:00:45 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-24 13:02:34 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-24 13:04:48 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-24 13:03:58 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-24 12:06:12 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-02-24 12:04:36 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-24 13:00:19 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-02-24 13:04:12 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-02-24 13:01:58 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-02-24 13:01:03 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-02-24 13:04:25 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-02-24 10:38:34 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | -0.013 |  |
| 2026-02-24 11:00:34 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.013 |  |
| 2026-02-24 12:07:08 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.019 |  |
| 2026-02-24 13:02:37 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -0.020 |  |
| 2026-02-24 13:02:54 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-02-24 13:03:04 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.021 |  |
| 2026-02-24 12:02:50 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.031 |  |
| 2026-02-24 12:06:01 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.058 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)