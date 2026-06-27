# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--27_13:18:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **190,782 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 13:18:30 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.026 |  |
| 2026-06-27 13:15:27 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:12:14 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-06-27 13:10:19 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-06-27 13:09:04 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 13:08:22 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-27 13:08:20 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:07:47 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-06-27 13:07:06 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:06:38 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-27 13:05:59 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:05:12 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:04:55 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:04:50 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:04:41 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | -0.029 |  |
| 2026-06-27 13:04:31 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-06-27 13:04:12 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:04:11 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.019 |  |
| 2026-06-27 13:03:54 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:03:49 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:03:29 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:03:28 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.010 |  |
| 2026-06-27 13:03:28 | Ellagawa (Kalu Ganga) | 5.32 | 🟢 Normal | -0.020 |  |
| 2026-06-27 13:02:36 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:02:31 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 13:02:29 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 13:02:24 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 13:02:17 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:02:16 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.99 | 🟢 Normal | -0.011 |  |
| 2026-06-27 13:01:37 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-27 13:01:36 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:01:30 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:01:24 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:01:17 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:00:57 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:00:50 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-06-27 13:00:37 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 13:08:22 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-27 13:01:37 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-27 13:10:19 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-06-27 13:06:38 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-27 13:02:24 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 13:02:29 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 13:02:31 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 13:09:04 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 13:01:17 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:01:36 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:01:30 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:03:49 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:01:24 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:04:50 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:03:29 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:02:16 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:03:54 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:02:36 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:05:59 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:15:27 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:04:55 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:04:12 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:00:57 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:05:12 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:08:20 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:07:06 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-27 12:08:01 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:02:17 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-06-27 13:12:14 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-06-27 13:07:47 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-06-27 13:03:28 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.010 |  |
| 2026-06-27 13:04:31 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-06-27 13:00:50 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-06-27 13:00:37 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-06-27 13:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.99 | 🟢 Normal | -0.011 |  |
| 2026-06-27 13:04:11 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.019 |  |
| 2026-06-27 13:03:28 | Ellagawa (Kalu Ganga) | 5.32 | 🟢 Normal | -0.020 |  |
| 2026-06-27 13:18:30 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.026 |  |
| 2026-06-27 13:04:41 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | -0.029 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)