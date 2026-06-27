# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--27_12:12:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **190,744 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 12:12:32 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 12:09:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:09:48 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.029 |  |
| 2026-06-27 12:08:01 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:07:18 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-27 12:07:04 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-27 12:06:16 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | -0.010 |  |
| 2026-06-27 12:06:15 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:06:11 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:05:51 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:04:56 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:04:53 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:04:33 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-06-27 12:04:31 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:04:18 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:04:16 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-27 12:04:02 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-27 12:03:49 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:03:38 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:03:25 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:03:24 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:03:10 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-06-27 12:03:06 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | -0.041 |  |
| 2026-06-27 12:02:55 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:02:53 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:02:40 | Ellagawa (Kalu Ganga) | 5.34 | 🟢 Normal | -0.020 |  |
| 2026-06-27 12:02:34 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-27 12:02:27 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 12:02:24 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:02:17 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-06-27 12:02:16 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.020 |  |
| 2026-06-27 12:01:56 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:01:48 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.242 |  |
| 2026-06-27 12:01:37 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-06-27 12:01:33 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:01:15 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-06-27 12:01:13 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:01:11 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:00:43 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-27 12:00:40 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 12:01:37 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-06-27 12:01:15 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-06-27 12:07:04 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-27 12:07:18 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-27 12:00:43 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-27 12:04:16 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-27 12:02:34 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-27 12:12:32 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 12:02:27 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 12:01:11 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:03:25 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:03:49 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:01:33 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:02:24 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:02:55 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:04:56 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:04:31 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:05:51 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:06:15 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:03:24 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:00:40 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:04:18 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:03:38 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:06:11 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:01:56 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:04:53 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:01:13 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:08:01 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:09:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:06:16 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | -0.010 |  |
| 2026-06-27 12:02:17 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-06-27 12:03:10 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-06-27 12:04:02 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-27 12:04:33 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-06-27 12:02:16 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.020 |  |
| 2026-06-27 12:02:40 | Ellagawa (Kalu Ganga) | 5.34 | 🟢 Normal | -0.020 |  |
| 2026-06-27 12:09:48 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.029 |  |
| 2026-06-27 12:03:06 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | -0.041 |  |
| 2026-06-27 12:01:48 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.242 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)