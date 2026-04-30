# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_20:14:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **139,388 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 20:14:30 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.013 |  |
| 2026-04-30 20:13:51 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 20:12:35 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -0.009 |  |
| 2026-04-30 20:11:04 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.071 |  |
| 2026-04-30 20:10:43 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | -0.019 |  |
| 2026-04-30 20:10:00 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-30 20:09:38 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-30 20:08:57 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-30 20:08:32 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | -0.009 |  |
| 2026-04-30 20:08:18 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.011 |  |
| 2026-04-30 20:08:08 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | -0.052 |  |
| 2026-04-30 20:08:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.01 | 🟢 Normal | -0.009 |  |
| 2026-04-30 20:07:16 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | -0.030 |  |
| 2026-04-30 20:06:45 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.056 |  |
| 2026-04-30 20:06:11 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-04-30 20:05:58 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | -0.030 |  |
| 2026-04-30 20:05:19 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-30 20:04:42 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-30 20:03:43 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-30 20:03:30 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-30 20:03:24 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-30 20:03:18 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.054 |  |
| 2026-04-30 20:02:34 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-04-30 20:02:31 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 20:02:23 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-04-30 20:01:30 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-30 20:06:11 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-04-30 20:09:38 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-30 20:04:42 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-30 20:01:15 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-30 20:03:24 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-30 20:08:57 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-30 20:03:43 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-30 20:01:50 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | 0.000 |  |
| 2026-04-30 20:02:03 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-30 20:03:30 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-30 20:05:19 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-30 20:10:00 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-30 20:02:25 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-30 20:01:08 | Rathnapura (Kalu Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:02:32 | Thanthirimale (Malwathu Oya) | 3.03 | 🟢 Normal | 0.000 |  |
| 2026-04-30 20:13:51 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 20:01:36 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-30 20:12:35 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -0.009 |  |
| 2026-04-30 20:08:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.01 | 🟢 Normal | -0.009 |  |
| 2026-04-30 20:08:32 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | -0.009 |  |
| 2026-04-30 20:02:34 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-04-30 20:01:06 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:02:01 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:03:14 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-30 20:08:18 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.011 |  |
| 2026-04-30 20:14:30 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.013 |  |
| 2026-04-30 20:10:43 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | -0.019 |  |
| 2026-04-30 20:01:59 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.027 |  |
| 2026-04-30 20:05:58 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | -0.030 |  |
| 2026-04-30 20:02:31 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.030 |  |
| 2026-04-30 20:07:16 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | -0.030 |  |
| 2026-04-30 19:01:48 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.031 |  |
| 2026-04-30 20:08:08 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | -0.052 |  |
| 2026-04-30 20:03:18 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.054 |  |
| 2026-04-30 20:06:45 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.056 |  |
| 2026-04-30 20:01:09 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.062 |  |
| 2026-04-30 20:11:04 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.071 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)