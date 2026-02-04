# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--04_09:04:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **63,886 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-04 09:04:48 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | -0.040 |  |
| 2026-02-04 09:04:37 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.900 | 🔺 Rising |
| 2026-02-04 09:04:36 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-04 09:04:36 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-04 09:04:35 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-02-04 09:04:31 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-04 09:04:29 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.097 |  |
| 2026-02-04 09:04:07 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-04 09:03:57 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.900 | 🔺 Rising |
| 2026-02-04 09:03:42 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.029 |  |
| 2026-02-04 09:03:14 | Weraganthota (Mahaweli Ganga) | -2.20 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-02-04 09:03:12 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-04 09:03:02 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-04 09:02:48 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-04 09:02:45 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-04 09:02:42 | Manampitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.048 |  |
| 2026-02-04 09:02:32 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-04 09:02:17 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.013 |  |
| 2026-02-04 09:02:17 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-02-04 09:02:11 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-04 09:02:10 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-04 09:01:35 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-04 09:01:32 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.033 |  |
| 2026-02-04 09:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-04 09:01:10 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:16:12 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.013 |  |
| 2026-02-04 08:09:46 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-04 09:04:37 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.900 | 🔺 Rising |
| 2026-02-04 09:03:14 | Weraganthota (Mahaweli Ganga) | -2.20 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-04 09:04:31 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-04 09:02:32 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-04 09:03:02 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-04 09:01:10 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-04 09:02:11 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:01:29 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-04 09:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-04 07:15:47 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-04 09:02:48 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-04 09:04:07 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-04 09:01:35 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:02:17 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-04 09:02:45 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-04 09:03:12 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-04 09:04:36 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-04 09:02:10 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-04 09:04:36 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:13:11⌛ | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-04 08:05:41 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-02-04 09:02:17 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-02-04 09:04:35 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-02-04 09:02:17 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.013 |  |
| 2026-02-04 06:02:42 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-02-02 18:03:26⌛ | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.021 |  |
| 2026-02-03 09:01:34⌛ | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.022 |  |
| 2026-02-04 09:03:42 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.029 |  |
| 2026-02-04 09:01:32 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.033 |  |
| 2026-02-04 09:04:48 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | -0.040 |  |
| 2026-02-04 09:02:42 | Manampitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.048 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-04 08:01:43 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.075 |  |
| 2026-02-04 09:04:29 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.097 |  |
| 2026-02-03 22:06:20 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.110 |  |
| 2026-02-04 08:04:16 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.114 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)