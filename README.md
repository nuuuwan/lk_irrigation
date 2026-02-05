# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--05_10:29:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **64,659 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-05 10:29:02 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-05 10:16:34 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.046 |  |
| 2026-02-05 10:14:15 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-05 10:13:24 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-05 10:11:24 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-05 10:07:38 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-05 10:06:09 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-05 10:06:00 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-02-05 10:05:57 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.040 |  |
| 2026-02-05 10:05:26 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-05 10:04:17 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.031 |  |
| 2026-02-05 10:03:45 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.011 |  |
| 2026-02-05 10:03:43 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-05 10:03:38 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-05 10:03:34 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 10:03:10 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.062 |  |
| 2026-02-05 10:02:56 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-02-05 10:02:53 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-05 10:02:37 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-05 10:02:33 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-02-05 10:02:26 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.257 | 🔺 Rising |
| 2026-02-05 10:02:24 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 10:02:23 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-05 10:02:23 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-05 10:02:06 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-05 10:02:01 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-05 10:01:48 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-05 10:00:48 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-05 10:00:38 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | 0.319 | 🔺 Rising |
| 2026-02-05 10:00:38 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-05 10:00:38 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | 0.319 | 🔺 Rising |
| 2026-02-05 10:02:26 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.257 | 🔺 Rising |
| 2026-02-05 10:02:56 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-05 06:07:34 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-05 10:00:48 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-05 10:05:26 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-05 10:14:15 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-05 10:02:24 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 10:03:34 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 10:01:48 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-05 10:02:53 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-05 10:06:09 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-05 10:00:38 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-05 10:11:24 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-05 10:13:24 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-05 10:29:02 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-05 10:02:37 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-05 10:02:23 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-05 10:02:06 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-05 10:02:01 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-05 10:03:38 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-05 10:07:38 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-05 10:03:43 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-05 10:02:23 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:13:11⌛ | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-05 10:06:00 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-02-05 10:02:33 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-02-05 10:03:45 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.011 |  |
| 2026-02-02 18:03:26⌛ | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.021 |  |
| 2026-02-05 09:03:47 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.030 |  |
| 2026-02-05 10:04:17 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.031 |  |
| 2026-02-05 10:05:57 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.040 |  |
| 2026-02-05 10:16:34 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.046 |  |
| 2026-02-05 10:03:10 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.062 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-03 22:06:20⌛ | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)