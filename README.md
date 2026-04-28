# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_09:18:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **137,188 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 09:18:48 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-28 09:11:56 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-28 09:11:05 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.108 |  |
| 2026-04-28 09:10:37 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.009 |  |
| 2026-04-28 09:09:54 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-28 09:09:28 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-04-28 09:07:49 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-28 09:07:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.074 |  |
| 2026-04-28 09:06:42 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.057 |  |
| 2026-04-28 09:06:37 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.060 |  |
| 2026-04-28 09:06:19 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-28 09:06:00 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 09:05:52 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-28 09:05:40 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-04-28 09:05:35 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-04-28 09:05:22 | Glencourse (Kelani Ganga) | 9.13 | 🟢 Normal | -0.076 |  |
| 2026-04-28 09:05:06 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-28 09:05:04 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-28 09:05:04 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | -0.038 |  |
| 2026-04-28 09:04:57 | Ellagawa (Kalu Ganga) | 4.59 | 🟢 Normal | -0.021 |  |
| 2026-04-28 09:04:51 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-04-28 09:04:37 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-28 09:04:31 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.011 |  |
| 2026-04-28 09:03:41 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-04-28 09:03:15 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-04-28 09:03:07 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-28 09:02:59 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 09:02:53 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 09:02:49 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.021 |  |
| 2026-04-28 09:02:42 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-28 09:02:31 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-04-28 09:02:18 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-28 09:02:16 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-28 09:02:12 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 09:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-28 09:01:48 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-04-28 09:01:43 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | -0.012 |  |
| 2026-04-28 09:00:15 | Manampitiya (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 09:00:12 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.033 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 09:03:41 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-04-28 09:18:48 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-28 09:05:52 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-28 09:04:37 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-28 09:07:49 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-28 09:02:16 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-28 09:02:53 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 09:02:59 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 09:06:19 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-28 09:00:15 | Manampitiya (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 09:02:12 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 09:04:51 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-04-28 09:06:00 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 09:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-28 09:09:54 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-28 09:11:56 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-28 09:03:07 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-28 09:02:42 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-28 09:05:06 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-28 09:02:18 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-28 09:10:37 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.009 |  |
| 2026-04-28 09:05:04 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-28 09:05:35 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-04-28 09:09:28 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-04-28 09:02:31 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-04-28 09:01:48 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-04-28 09:04:31 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.011 |  |
| 2026-04-28 09:01:43 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | -0.012 |  |
| 2026-04-28 09:05:40 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-04-28 09:03:15 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-04-28 09:02:49 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.021 |  |
| 2026-04-28 09:04:57 | Ellagawa (Kalu Ganga) | 4.59 | 🟢 Normal | -0.021 |  |
| 2026-04-28 09:00:12 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.033 |  |
| 2026-04-28 09:05:04 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | -0.038 |  |
| 2026-04-28 09:06:42 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.057 |  |
| 2026-04-28 09:06:37 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.060 |  |
| 2026-04-28 09:07:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.074 |  |
| 2026-04-28 09:05:22 | Glencourse (Kelani Ganga) | 9.13 | 🟢 Normal | -0.076 |  |
| 2026-04-28 09:11:05 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.108 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)