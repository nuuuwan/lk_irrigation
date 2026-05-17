# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_08:13:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **154,118 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 08:13:13 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.019 |  |
| 2026-05-17 08:09:57 | Magura (Kalu Ganga) | 3.21 | 🟢 Normal | -0.029 |  |
| 2026-05-17 08:08:52 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 08:08:34 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-05-17 08:08:27 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-17 08:08:22 | Rathnapura (Kalu Ganga) | 3.37 | 🟢 Normal | -0.047 |  |
| 2026-05-17 08:07:33 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-05-17 08:07:26 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-05-17 08:06:38 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.011 |  |
| 2026-05-17 08:06:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.80 | 🟠 Minor Flood | -0.010 |  |
| 2026-05-17 08:06:26 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-17 08:06:04 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -0.010 |  |
| 2026-05-17 08:05:59 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-05-17 08:05:43 | Hanwella (Kelani Ganga) | 3.36 | 🟢 Normal | -0.049 |  |
| 2026-05-17 08:05:42 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-17 08:04:20 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-17 08:04:11 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 08:03:57 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-17 08:03:43 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-17 08:03:33 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-17 08:03:33 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.031 |  |
| 2026-05-17 08:03:29 | Baddegama (Gin Ganga) | 2.41 | 🟢 Normal | -0.021 |  |
| 2026-05-17 08:03:13 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.015 |  |
| 2026-05-17 08:03:12 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | -0.059 |  |
| 2026-05-17 08:02:54 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-05-17 08:02:54 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 08:02:46 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-17 08:02:38 | Panadugama (Nilwala Ganga) | 3.12 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-17 08:01:55 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.031 |  |
| 2026-05-17 08:01:51 | Moragaswewa (Deduru Oya) | 1.49 | 🟢 Normal | -0.064 |  |
| 2026-05-17 08:01:49 | Galgamuwa (Mee Oya) | 1.84 | 🟢 Normal | -0.021 |  |
| 2026-05-17 08:01:48 | Thanthirimale (Malwathu Oya) | 3.70 | 🟢 Normal | -0.021 |  |
| 2026-05-17 08:01:40 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.030 |  |
| 2026-05-17 08:01:24 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-17 08:01:16 | Ellagawa (Kalu Ganga) | 7.90 | 🟢 Normal | -0.020 |  |
| 2026-05-17 08:01:09 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-17 08:00:45 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-05-17 08:00:41 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 08:06:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.80 | 🟠 Minor Flood | -0.010 |  |
| 2026-05-17 08:01:09 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-05-17 08:03:57 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-17 08:02:38 | Panadugama (Nilwala Ganga) | 3.12 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-17 08:02:54 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 08:08:52 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 08:04:11 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 08:02:46 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-17 08:00:41 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-17 08:00:45 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-05-17 08:06:26 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-17 08:03:33 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-17 08:07:33 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-05-17 08:07:26 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-05-17 08:03:43 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-17 08:01:24 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-17 08:08:27 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-17 08:05:42 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-17 08:06:04 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -0.010 |  |
| 2026-05-17 08:08:34 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-05-17 08:02:54 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-05-17 08:05:59 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-05-17 08:04:20 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-17 08:00:13 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-05-17 08:06:38 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.011 |  |
| 2026-05-17 08:03:13 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.015 |  |
| 2026-05-17 08:13:13 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.019 |  |
| 2026-05-17 08:01:16 | Ellagawa (Kalu Ganga) | 7.90 | 🟢 Normal | -0.020 |  |
| 2026-05-17 08:03:29 | Baddegama (Gin Ganga) | 2.41 | 🟢 Normal | -0.021 |  |
| 2026-05-17 08:01:49 | Galgamuwa (Mee Oya) | 1.84 | 🟢 Normal | -0.021 |  |
| 2026-05-17 08:01:48 | Thanthirimale (Malwathu Oya) | 3.70 | 🟢 Normal | -0.021 |  |
| 2026-05-17 08:09:57 | Magura (Kalu Ganga) | 3.21 | 🟢 Normal | -0.029 |  |
| 2026-05-17 08:01:40 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.030 |  |
| 2026-05-17 08:03:33 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.031 |  |
| 2026-05-17 08:01:55 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.031 |  |
| 2026-05-17 08:08:22 | Rathnapura (Kalu Ganga) | 3.37 | 🟢 Normal | -0.047 |  |
| 2026-05-17 08:05:43 | Hanwella (Kelani Ganga) | 3.36 | 🟢 Normal | -0.049 |  |
| 2026-05-17 08:03:12 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | -0.059 |  |
| 2026-05-17 08:01:51 | Moragaswewa (Deduru Oya) | 1.49 | 🟢 Normal | -0.064 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)