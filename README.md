# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_06:21:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **112,078 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-31 06:21:48 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-03-31 06:14:31 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:12:40 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | -0.009 |  |
| 2026-03-31 06:11:34 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:10:22 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-03-31 06:08:36 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | -0.009 |  |
| 2026-03-31 06:07:06 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:06:47 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.146 |  |
| 2026-03-31 06:06:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.043 |  |
| 2026-03-31 06:05:53 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | -0.023 |  |
| 2026-03-31 06:05:45 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.078 |  |
| 2026-03-31 06:04:58 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.037 |  |
| 2026-03-31 06:04:32 | Ellagawa (Kalu Ganga) | 3.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-31 06:04:17 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:04:16 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:04:14 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-03-31 06:03:41 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.030 |  |
| 2026-03-31 06:03:07 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.014 |  |
| 2026-03-31 06:03:07 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:03:02 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:02:40 | Hanwella (Kelani Ganga) | 0.16 | 🟢 Normal | -0.041 |  |
| 2026-03-31 06:02:38 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:02:31 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:02:28 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-31 06:02:28 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-03-31 06:02:12 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.013 |  |
| 2026-03-31 06:02:08 | Manampitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.072 |  |
| 2026-03-31 06:01:52 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:01:47 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.444 | 🔺 Rising |
| 2026-03-31 06:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.040 |  |
| 2026-03-31 06:01:15 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:00:49 | Weraganthota (Mahaweli Ganga) | -2.20 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-03-31 06:00:46 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:00:46 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:00:12 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:00:10 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-31 06:01:47 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.444 | 🔺 Rising |
| 2026-03-31 06:00:49 | Weraganthota (Mahaweli Ganga) | -2.20 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-03-31 06:04:14 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-03-31 06:04:32 | Ellagawa (Kalu Ganga) | 3.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-30 18:07:18 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-31 06:21:48 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-03-31 05:02:17 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-03-31 06:01:15 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:02:31 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:03:07 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:00:46 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:11:34 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:02:38 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:04:17 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:00:46 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:00:12 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:03:02 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:07:06 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:04:16 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:00:31 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:09:23 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:14:31 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:12:40 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | -0.009 |  |
| 2026-03-31 06:08:36 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | -0.009 |  |
| 2026-03-31 06:02:28 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-31 06:02:28 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-03-31 06:10:22 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-03-31 06:00:10 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.012 |  |
| 2026-03-31 06:02:12 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.013 |  |
| 2026-03-31 06:03:07 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.014 |  |
| 2026-03-31 06:05:53 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | -0.023 |  |
| 2026-03-31 06:03:41 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.030 |  |
| 2026-03-31 06:04:58 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.037 |  |
| 2026-03-31 06:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.040 |  |
| 2026-03-31 06:02:40 | Hanwella (Kelani Ganga) | 0.16 | 🟢 Normal | -0.041 |  |
| 2026-03-31 06:06:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.043 |  |
| 2026-03-31 06:02:08 | Manampitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.072 |  |
| 2026-03-31 06:05:45 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.078 |  |
| 2026-03-31 06:06:47 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.146 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)