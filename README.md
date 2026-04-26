# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_11:17:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **135,495 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 11:17:41 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:16:52 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:16:18 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | -0.017 |  |
| 2026-04-26 11:12:42 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.027 |  |
| 2026-04-26 11:10:09 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-04-26 11:09:09 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.336 | 🔺 Rising |
| 2026-04-26 11:08:56 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-26 11:08:55 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:08:53 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:08:15 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:07:34 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:05:19 | Katharagama (Menik Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-04-26 11:05:03 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-04-26 11:05:02 | Ellagawa (Kalu Ganga) | 4.33 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:05:00 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.030 |  |
| 2026-04-26 11:05:00 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-04-26 11:04:30 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:04:23 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:03:59 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:03:38 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:03:28 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.040 |  |
| 2026-04-26 11:03:01 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:02:57 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:02:56 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:02:44 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.307 | 🔺 Rising |
| 2026-04-26 11:02:35 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-04-26 11:02:33 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:02:32 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-04-26 11:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.050 |  |
| 2026-04-26 11:02:19 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.040 |  |
| 2026-04-26 11:01:55 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-26 11:01:25 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:01:23 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:01:10 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-04-26 11:01:09 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:00:46 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:00:40 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:00:16 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.049 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 09:02:52 | Urawa (Nilwala Ganga) | 4.00 | 🟠 Minor Flood | 1.986 | 🔺 Rising |
| 2026-04-26 11:09:09 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.336 | 🔺 Rising |
| 2026-04-26 11:02:44 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.307 | 🔺 Rising |
| 2026-04-26 11:08:56 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-26 11:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-26 11:02:56 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:01:23 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:00:40 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:17:41 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:02:57 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:04:23 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:03:59 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:03:38 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:05:02 | Ellagawa (Kalu Ganga) | 4.33 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:01:25 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:08:53 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:07:34 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:02:33 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:08:15 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:04:30 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:01:09 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:00:46 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:03:01 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:01:55 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:16:52 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-26 11:10:09 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-04-26 11:01:10 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-04-26 11:05:19 | Katharagama (Menik Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-04-26 11:02:32 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-04-26 11:05:00 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-04-26 11:05:03 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-04-26 11:16:18 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | -0.017 |  |
| 2026-04-26 11:02:35 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-04-26 11:12:42 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.027 |  |
| 2026-04-26 11:05:00 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.030 |  |
| 2026-04-26 11:02:19 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.040 |  |
| 2026-04-26 11:03:28 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.040 |  |
| 2026-04-26 11:00:16 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.049 |  |
| 2026-04-26 11:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)