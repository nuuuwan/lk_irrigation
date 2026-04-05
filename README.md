# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_04:12:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **117,388 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 04:12:06 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | -0.018 |  |
| 2026-04-06 04:11:18 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-04-06 04:10:45 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:07:57 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-04-06 04:07:11 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:05:20 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-04-06 04:04:29 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-04-06 04:04:27 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.011 |  |
| 2026-04-06 04:04:16 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:04:04 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.071 |  |
| 2026-04-06 04:03:59 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:03:10 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:02:49 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-04-06 04:02:49 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:02:43 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-04-06 04:02:42 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 04:02:42 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.340 | 🔺 Rising |
| 2026-04-06 04:02:30 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:02:23 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:02:18 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:01:55 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:01:37 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:01:14 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:01:13 | Peradeniya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.130 |  |
| 2026-04-06 04:01:12 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:00:58 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:00:42 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-04-06 04:00:41 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:41:45 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 04:02:42 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.340 | 🔺 Rising |
| 2026-04-06 04:07:57 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-04-06 04:00:42 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-04-06 02:07:58 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-06 04:02:42 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 04:10:45 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:01:55 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:02:03 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:02:30 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:02:18 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:08:03 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:03:49 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-06 00:01:54 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:02:49 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:02:23 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:00:58 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:07:11 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:04:16 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:01:14 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:03:59 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:03:32 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:03:10 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:01:37 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-06 04:11:18 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-04-06 04:05:20 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-04-06 03:41:45 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-04-06 04:04:29 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:02:03 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-06 04:02:43 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-04-06 04:04:27 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.011 |  |
| 2026-04-06 03:11:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.017 |  |
| 2026-04-06 04:12:06 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | -0.018 |  |
| 2026-04-06 04:02:49 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-04-06 03:05:45 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.025 |  |
| 2026-04-05 18:02:13 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.050 |  |
| 2026-04-06 04:04:04 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.071 |  |
| 2026-04-05 18:02:28 | Thanthirimale (Malwathu Oya) | 2.42 | 🟢 Normal | -0.088 |  |
| 2026-04-06 04:01:13 | Peradeniya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.130 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)