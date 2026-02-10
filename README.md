# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--10_13:06:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **69,266 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 13:06:14 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-10 13:05:52 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-02-10 13:05:40 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:05:08 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.019 |  |
| 2026-02-10 13:04:39 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:04:21 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:03:50 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-02-10 13:03:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-02-10 13:03:11 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:03:11 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:02:54 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:02:54 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:02:52 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-10 13:02:48 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-02-10 13:02:47 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-02-10 13:02:43 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-10 13:02:40 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:02:38 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.039 |  |
| 2026-02-10 13:02:36 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:02:32 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-02-10 13:02:20 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:02:07 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:02:06 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-10 13:02:01 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.031 |  |
| 2026-02-10 13:02:00 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | 0.484 | 🔺 Rising |
| 2026-02-10 13:01:53 | Nagalagam Street (Kelani Ganga) | 0.35 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-02-10 13:01:25 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:01:23 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:01:22 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:00:45 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-10 12:15:10 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | -0.009 |  |
| 2026-02-10 12:14:17 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-10 12:13:00 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -0.014 |  |
| 2026-02-10 12:12:21 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 13:02:00 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | 0.484 | 🔺 Rising |
| 2026-02-10 13:01:53 | Nagalagam Street (Kelani Ganga) | 0.35 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-02-10 12:01:34 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-02-10 13:02:43 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-10 13:02:52 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-10 13:06:14 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-10 13:02:20 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:02:40 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:01:22 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:02:36 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:03:11 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:04:39 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:02:54 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:01:25 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:02:07 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:04:21 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-10 12:01:13 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:05:40 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:03:11 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-10 12:08:07 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-10 12:02:52 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:02:54 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:00:45 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-10 12:14:17 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-10 13:01:23 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-10 12:06:00 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-10 12:15:10 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | -0.009 |  |
| 2026-02-10 13:02:47 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-02-10 13:03:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-02-10 13:02:48 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-02-10 13:02:06 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-10 13:05:52 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-02-10 13:02:32 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-02-10 13:03:50 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-02-10 12:13:00 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -0.014 |  |
| 2026-02-10 13:05:08 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.019 |  |
| 2026-02-10 12:08:33 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.028 |  |
| 2026-02-10 13:02:01 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.031 |  |
| 2026-02-10 13:02:38 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.039 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)