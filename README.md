# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_21:02:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **145,595 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 21:02:37 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.110 |  |
| 2026-05-07 21:02:34 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-05-07 21:02:07 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | 0.287 | 🔺 Rising |
| 2026-05-07 21:02:06 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-05-07 21:01:58 | Wellawaya (Kirindi Oya) | 2.05 | 🟢 Normal | -0.713 |  |
| 2026-05-07 21:01:51 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 21:01:46 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | -0.010 |  |
| 2026-05-07 21:01:30 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 21:01:17 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-05-07 21:01:16 | Kuda Oya (Kirindi Oya) | 3.38 | 🟢 Normal | -0.120 |  |
| 2026-05-07 20:51:55 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 20:26:43 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-07 20:20:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-05-07 20:10:54 | Manampitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-07 20:10:42 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.087 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 20:04:29 | Deraniyagala (Kelani Ganga) | 1.57 | 🟢 Normal | 1.029 | 🔺 Rising |
| 2026-05-07 20:09:02 | Holombuwa (Kelani Ganga) | 2.35 | 🟢 Normal | 1.022 | 🔺 Rising |
| 2026-05-07 20:01:41 | Pitabeddara (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.664 | 🔺 Rising |
| 2026-05-07 20:05:58 | Rathnapura (Kalu Ganga) | 2.26 | 🟢 Normal | 0.359 | 🔺 Rising |
| 2026-05-07 21:02:07 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | 0.287 | 🔺 Rising |
| 2026-05-07 20:05:45 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-05-07 20:01:15 | Panadugama (Nilwala Ganga) | 2.91 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-05-07 21:02:06 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-05-07 20:10:42 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-07 20:06:11 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-07 20:26:43 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-07 21:01:51 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 20:04:07 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 20:09:34 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-07 20:07:04 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-07 20:05:44 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-07 21:01:30 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 20:06:37 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-07 20:10:54 | Manampitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-07 20:20:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-05-07 18:02:03 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-05-07 20:08:13 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-05-07 21:01:17 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-05-07 21:02:34 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-05-07 21:01:46 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | -0.010 |  |
| 2026-05-07 20:02:14 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | -0.011 |  |
| 2026-05-07 20:05:54 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | -0.020 |  |
| 2026-05-07 18:02:13 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | -0.029 |  |
| 2026-05-07 20:06:32 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | -0.036 |  |
| 2026-05-07 20:06:42 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.040 |  |
| 2026-05-07 18:00:09 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | -0.063 |  |
| 2026-05-07 20:06:50 | Thanamalwila (Kirindi Oya) | 3.10 | 🟢 Normal | -0.070 |  |
| 2026-05-07 20:05:05 | Hanwella (Kelani Ganga) | 1.51 | 🟢 Normal | -0.079 |  |
| 2026-05-07 20:03:10 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.081 |  |
| 2026-05-07 20:03:18 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.088 |  |
| 2026-05-07 21:02:37 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.110 |  |
| 2026-05-07 20:09:49 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.115 |  |
| 2026-05-07 21:01:16 | Kuda Oya (Kirindi Oya) | 3.38 | 🟢 Normal | -0.120 |  |
| 2026-05-07 21:01:58 | Wellawaya (Kirindi Oya) | 2.05 | 🟢 Normal | -0.713 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)