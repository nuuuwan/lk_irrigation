# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_02:35:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **135,154 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 02:35:36 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.007 |  |
| 2026-04-26 02:28:29 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -1.091 |  |
| 2026-04-26 02:27:56 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -1.091 |  |
| 2026-04-26 02:12:01 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-26 02:09:10 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-04-26 02:08:19 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-26 02:07:17 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-26 02:07:01 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.013 |  |
| 2026-04-26 02:05:58 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-26 02:05:26 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.019 |  |
| 2026-04-26 02:04:44 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.020 |  |
| 2026-04-26 02:04:16 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | -0.021 |  |
| 2026-04-26 02:03:59 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.099 |  |
| 2026-04-26 02:03:58 | Peradeniya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.272 |  |
| 2026-04-26 02:03:57 | Katharagama (Menik Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-04-26 02:03:48 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-26 02:02:47 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.030 |  |
| 2026-04-26 02:02:35 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-26 02:02:21 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.011 |  |
| 2026-04-26 02:02:13 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-04-26 02:02:00 | Thaldena (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.282 |  |
| 2026-04-26 02:01:59 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-26 02:01:53 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.011 |  |
| 2026-04-26 02:01:38 | Moragaswewa (Deduru Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-26 02:01:28 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-04-26 02:01:14 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-04-26 02:00:37 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 00:07:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-26 02:12:01 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-26 02:07:17 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-26 01:01:52 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:01:38 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:02:03 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 02:01:59 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-26 02:05:58 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:01:52 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-26 02:02:35 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-26 02:08:19 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-26 01:01:11 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-26 02:35:36 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.007 |  |
| 2026-04-26 01:21:59 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-04-26 02:09:10 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-04-26 02:03:48 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-26 02:01:28 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-04-26 02:03:57 | Katharagama (Menik Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-04-26 02:01:38 | Moragaswewa (Deduru Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-26 02:01:14 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-04-26 02:02:21 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.011 |  |
| 2026-04-26 02:00:37 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-04-26 02:01:53 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.011 |  |
| 2026-04-26 01:48:38 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | -0.012 |  |
| 2026-04-26 02:07:01 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.013 |  |
| 2026-04-26 02:05:26 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.019 |  |
| 2026-04-26 02:02:13 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-04-25 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.020 |  |
| 2026-04-26 01:01:35 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | -0.020 |  |
| 2026-04-26 02:04:44 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.020 |  |
| 2026-04-26 02:04:16 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | -0.021 |  |
| 2026-04-25 18:01:09 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-04-26 02:02:47 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.030 |  |
| 2026-04-25 18:00:50 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.050 |  |
| 2026-04-26 01:29:07 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.061 |  |
| 2026-04-26 02:03:59 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.099 |  |
| 2026-04-26 02:03:58 | Peradeniya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.272 |  |
| 2026-04-26 02:02:00 | Thaldena (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.282 |  |
| 2026-04-26 02:28:29 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -1.091 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)