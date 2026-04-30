# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_16:17:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **139,236 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 16:17:53 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-30 16:11:33 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-04-30 16:10:40 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:10:03 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:09:19 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-30 16:09:07 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-04-30 16:08:55 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:08:35 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-04-30 16:08:13 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:07:32 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:07:07 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:06:56 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-30 16:06:55 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.019 |  |
| 2026-04-30 16:06:53 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.065 |  |
| 2026-04-30 16:06:24 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:05:10 | Ellagawa (Kalu Ganga) | 4.43 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:04:52 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:04:41 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:04:38 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:04:14 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:04:01 | Peradeniya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-04-30 16:03:59 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-30 16:03:39 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.040 |  |
| 2026-04-30 16:03:15 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-30 16:03:14 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-30 16:02:53 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-30 16:02:52 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:02:50 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-04-30 16:02:38 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | -0.021 |  |
| 2026-04-30 16:02:16 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:02:15 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | -0.030 |  |
| 2026-04-30 16:01:38 | Thanthirimale (Malwathu Oya) | 3.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-30 16:01:38 | Dunamale (Aththanagalu Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:01:36 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:01:28 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:01:26 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-30 16:01:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | -0.013 |  |
| 2026-04-30 16:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-04-30 16:00:38 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:00:19 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-30 15:59:47 | Dunamale (Aththanagalu Oya) | 0.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 16:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-04-30 16:03:14 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-30 16:02:53 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-30 16:06:56 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-30 16:01:38 | Thanthirimale (Malwathu Oya) | 3.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-30 16:09:19 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-30 16:01:26 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-30 16:17:53 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-30 16:00:38 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:00:19 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:02:16 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:07:07 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:04:41 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:07:32 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:04:14 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:05:10 | Ellagawa (Kalu Ganga) | 4.43 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:01:28 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:10:40 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:06:24 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:01:38 | Dunamale (Aththanagalu Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:08:13 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:02:52 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:08:55 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:10:03 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:04:52 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-30 16:08:35 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-04-30 16:02:50 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-04-30 15:03:15 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-04-30 16:11:33 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-04-30 16:03:59 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-30 16:03:15 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-30 16:04:01 | Peradeniya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-04-30 16:01:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | -0.013 |  |
| 2026-04-30 16:06:55 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.019 |  |
| 2026-04-30 16:09:07 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-04-30 16:02:38 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | -0.021 |  |
| 2026-04-30 16:02:15 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | -0.030 |  |
| 2026-04-30 16:03:39 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.040 |  |
| 2026-04-30 16:06:53 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.065 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)