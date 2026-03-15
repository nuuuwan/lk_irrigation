# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--16_04:18:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **98,587 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 04:18:03 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:16:05 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-16 04:14:10 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-16 04:11:14 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:10:12 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.066 |  |
| 2026-03-16 04:09:48 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.053 |  |
| 2026-03-16 04:09:06 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:07:26 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-03-16 04:06:21 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-03-16 04:06:14 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:05:19 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-16 04:04:56 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.022 |  |
| 2026-03-16 04:03:59 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:03:52 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | -0.038 |  |
| 2026-03-16 04:03:51 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-03-16 04:03:31 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.051 |  |
| 2026-03-16 04:03:13 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:03:07 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-16 04:03:02 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.005 |  |
| 2026-03-16 04:02:59 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:02:48 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:02:36 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:02:32 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:02:05 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-03-16 04:01:59 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:01:42 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:01:36 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.126 |  |
| 2026-03-16 04:01:11 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 04:01:10 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.021 |  |
| 2026-03-16 04:00:57 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:00:38 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-03-16 04:00:30 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 03:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 1.662 | 🔺 Rising |
| 2026-03-16 04:16:05 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-16 04:14:10 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-16 04:05:19 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-16 04:03:07 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-16 04:01:11 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 03:02:47 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 04:09:06 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:02:59 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:01:42 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:05:04 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-16 03:01:45 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:02:36 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:03:13 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:18:03 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-03-16 03:07:38 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:00:30 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:02:48 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:00:57 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:11:14 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:02:20 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:06:14 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:01:59 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:02:32 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:03:02 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.005 |  |
| 2026-03-16 04:03:51 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-03-16 04:07:26 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-03-16 04:00:38 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-03-16 04:02:05 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-03-16 04:01:10 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.021 |  |
| 2026-03-16 04:04:56 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.022 |  |
| 2026-03-16 04:06:21 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-03-16 04:03:52 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | -0.038 |  |
| 2026-03-15 18:02:59 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.040 |  |
| 2026-03-16 04:03:31 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.051 |  |
| 2026-03-16 04:09:48 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.053 |  |
| 2026-03-16 04:10:12 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.066 |  |
| 2026-03-16 04:01:36 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.126 |  |
| 2026-03-16 03:08:20 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)