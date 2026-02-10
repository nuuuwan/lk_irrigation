# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--10_16:13:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **69,386 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 16:13:09 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | -0.009 |  |
| 2026-02-10 16:12:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:09:13 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-10 16:08:47 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | -0.009 |  |
| 2026-02-10 16:07:54 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | -0.019 |  |
| 2026-02-10 16:07:54 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:07:43 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:06:23 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.030 |  |
| 2026-02-10 16:06:20 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:06:13 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:05:49 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:05:17 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-02-10 16:04:50 | Kithulgala (Kelani Ganga) | 1.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-10 16:03:52 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:03:46 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:03:30 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:03:17 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | -0.013 |  |
| 2026-02-10 16:03:08 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-02-10 16:02:54 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:02:51 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-10 16:02:49 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | -0.029 |  |
| 2026-02-10 16:02:48 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.076 |  |
| 2026-02-10 16:02:47 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:02:28 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-02-10 16:02:08 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:01:55 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:01:45 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-02-10 16:01:36 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:01:19 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:01:14 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-02-10 16:01:10 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:01:05 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-02-10 16:00:22 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-10 15:25:54 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 16:05:17 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-02-10 16:01:45 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-02-10 16:04:50 | Kithulgala (Kelani Ganga) | 1.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-10 16:02:51 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-10 16:09:13 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-10 16:01:36 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:02:47 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:03:30 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:01:55 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:06:20 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-10 15:05:33 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:03:52 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:03:46 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-10 15:03:45 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-10 15:04:04 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:07:43 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:00:22 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:02:54 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:01:19 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:02:08 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:06:13 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:05:49 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-10 15:05:56 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:07:54 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-10 15:03:17 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:01:10 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:12:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-02-10 16:08:47 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | -0.009 |  |
| 2026-02-10 16:13:09 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | -0.009 |  |
| 2026-02-10 16:02:28 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-02-10 16:01:05 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-02-10 16:03:08 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-02-10 16:01:14 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-02-10 16:03:17 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | -0.013 |  |
| 2026-02-10 16:07:54 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | -0.019 |  |
| 2026-02-10 15:07:00 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.021 |  |
| 2026-02-10 16:02:49 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | -0.029 |  |
| 2026-02-10 16:06:23 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.030 |  |
| 2026-02-10 16:02:48 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.076 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)