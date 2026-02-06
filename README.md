# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--06_13:26:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **65,622 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 13:26:03 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:25:23 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.041 |  |
| 2026-02-06 13:23:45 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-02-06 13:20:14 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-06 13:19:29 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 1.709 | 🔺 Rising |
| 2026-02-06 13:15:33 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:10:01 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:07:55 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | -0.009 |  |
| 2026-02-06 13:07:07 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:07:04 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.156 |  |
| 2026-02-06 13:06:33 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-06 13:05:34 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:05:10 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:04:55 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-06 13:04:42 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:04:28 | Padiyathalawa (Maduru Oya) | 1.60 | 🟢 Normal | -0.124 |  |
| 2026-02-06 13:04:13 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-02-06 13:03:48 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:03:46 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:03:15 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | -0.040 |  |
| 2026-02-06 13:02:55 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-02-06 13:02:53 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:02:32 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-02-06 13:02:31 | Dunamale (Aththanagalu Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:02:27 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:02:27 | Manampitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-06 13:01:59 | Weraganthota (Mahaweli Ganga) | -2.06 | 🟢 Normal | -0.050 |  |
| 2026-02-06 13:01:57 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-06 13:01:56 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-02-06 13:01:46 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-02-06 13:01:13 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-02-06 13:01:13 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:01:08 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-06 13:00:44 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-02-06 12:41:07 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.041 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 13:19:29 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 1.709 | 🔺 Rising |
| 2026-02-06 13:00:44 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-06 13:01:57 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-06 06:05:56 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-06 13:04:55 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-06 13:02:27 | Manampitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-06 13:01:08 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-06 13:06:33 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-06 13:20:14 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-06 13:23:45 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-02-06 12:10:22 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-02-06 13:05:34 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:01:13 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:02:53 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:10:01 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:26:03 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:02:31 | Dunamale (Aththanagalu Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:02:27 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:05:10 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:07:07 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:03:46 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:04:42 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:15:33 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-06 13:07:55 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | -0.009 |  |
| 2026-02-06 13:02:32 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-02-06 13:01:56 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-02-06 13:01:46 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-02-06 13:01:13 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-02-06 13:02:55 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-02-06 13:04:13 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-02-06 13:03:15 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | -0.040 |  |
| 2026-02-06 13:25:23 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.041 |  |
| 2026-02-06 13:01:59 | Weraganthota (Mahaweli Ganga) | -2.06 | 🟢 Normal | -0.050 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-06 13:04:28 | Padiyathalawa (Maduru Oya) | 1.60 | 🟢 Normal | -0.124 |  |
| 2026-02-06 13:07:04 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.156 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)