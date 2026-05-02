# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_01:44:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **141,351 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 01:44:18 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.006 |  |
| 2026-05-03 01:20:55 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-03 01:20:24 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-03 01:18:02 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-03 01:17:26 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.025 |  |
| 2026-05-03 01:07:09 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-03 01:06:30 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-03 01:06:10 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.009 |  |
| 2026-05-03 01:05:57 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.019 |  |
| 2026-05-03 01:05:33 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-03 01:05:11 | Rathnapura (Kalu Ganga) | 1.79 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-05-03 01:03:46 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-03 01:03:46 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-05-03 01:03:31 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-03 01:03:25 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-05-03 01:03:14 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-05-03 01:02:22 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-03 01:02:16 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-03 01:02:09 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-05-03 01:01:57 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-05-03 01:01:55 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-03 01:01:55 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.021 |  |
| 2026-05-03 01:01:55 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-03 01:01:47 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-03 01:01:42 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | 0.000 |  |
| 2026-05-03 01:01:39 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-03 01:01:33 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-05-03 01:01:19 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-03 01:00:33 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-03 01:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.748 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 01:05:11 | Rathnapura (Kalu Ganga) | 1.79 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-05-02 23:26:39 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-05-02 18:01:54 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-03 01:00:33 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-03 01:07:09 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-03 01:01:19 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-03 01:02:22 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-03 01:01:55 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-03 01:01:39 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-03 01:01:47 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-03 01:01:55 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 21:01:17 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:01:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-03 01:05:33 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-03 00:08:05 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-05-03 01:01:42 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | 0.000 |  |
| 2026-05-03 01:20:55 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-03 00:06:16 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-03 01:02:16 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-03 01:18:02 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-03 01:20:24 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-03 01:03:46 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-03 01:44:18 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.006 |  |
| 2026-05-03 01:06:10 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.009 |  |
| 2026-05-03 01:03:46 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-05-02 18:01:54 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-05-03 01:01:57 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-05-03 01:01:33 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-05-03 01:03:14 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-05-03 01:02:09 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-05-03 01:03:25 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-05-03 00:03:06 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-05-03 01:05:57 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.019 |  |
| 2026-05-03 01:01:55 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.021 |  |
| 2026-05-03 01:17:26 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.025 |  |
| 2026-05-03 00:02:30 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.050 |  |
| 2026-05-02 20:09:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.141 |  |
| 2026-05-03 01:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.748 |  |
| 2026-05-03 00:18:31 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)