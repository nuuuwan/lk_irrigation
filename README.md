# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--14_07:03:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **178,915 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 07:03:16 | Hanwella (Kelani Ganga) | 3.70 | 🟢 Normal | -0.052 |  |
| 2026-06-14 07:03:13 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-06-14 07:03:11 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.030 |  |
| 2026-06-14 07:03:01 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.090 |  |
| 2026-06-14 07:02:59 | Giriulla (Maha Oya) | 2.00 | 🟢 Normal | -0.030 |  |
| 2026-06-14 07:02:52 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-06-14 07:02:50 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.054 |  |
| 2026-06-14 07:02:47 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | -0.010 |  |
| 2026-06-14 07:02:34 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-14 07:02:18 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-14 07:02:13 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-06-14 07:01:34 | Ellagawa (Kalu Ganga) | 8.54 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-14 07:01:23 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.121 |  |
| 2026-06-14 07:01:20 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-14 07:01:18 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-06-14 07:01:17 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-14 07:00:11 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.040 |  |
| 2026-06-14 06:27:46 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | -0.060 |  |
| 2026-06-14 06:16:02 | Holombuwa (Kelani Ganga) | 1.09 | 🟢 Normal | -0.037 |  |
| 2026-06-14 06:15:33 | Dunamale (Aththanagalu Oya) | 3.17 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 06:07:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.47 | 🟡 Alert | -0.117 |  |
| 2026-06-13 18:01:49 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-14 07:01:34 | Ellagawa (Kalu Ganga) | 8.54 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-14 07:01:20 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-14 07:01:17 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-14 07:02:18 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-14 07:02:34 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-14 06:08:17 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-14 06:00:56 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-06-14 06:01:47 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-14 06:00:10 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-14 06:15:33 | Dunamale (Aththanagalu Oya) | 3.17 | 🟢 Normal | 0.000 |  |
| 2026-06-14 06:03:07 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-06-14 06:06:29 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-06-14 07:02:47 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | -0.010 |  |
| 2026-06-14 07:02:52 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-06-14 07:01:18 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-06-14 06:02:12 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-06-14 06:02:12 | Badalgama (Maha Oya) | 3.22 | 🟢 Normal | -0.010 |  |
| 2026-06-14 07:02:13 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-06-14 07:03:13 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-06-14 06:08:34 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.018 |  |
| 2026-06-14 06:07:14 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.028 |  |
| 2026-06-14 07:02:59 | Giriulla (Maha Oya) | 2.00 | 🟢 Normal | -0.030 |  |
| 2026-06-14 07:03:11 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.030 |  |
| 2026-06-14 06:16:02 | Holombuwa (Kelani Ganga) | 1.09 | 🟢 Normal | -0.037 |  |
| 2026-06-14 07:00:11 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.040 |  |
| 2026-06-14 06:03:37 | Glencourse (Kelani Ganga) | 11.49 | 🟢 Normal | -0.041 |  |
| 2026-06-14 06:03:36 | Baddegama (Gin Ganga) | 2.96 | 🟢 Normal | -0.043 |  |
| 2026-06-14 06:06:26 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.048 |  |
| 2026-06-14 07:03:16 | Hanwella (Kelani Ganga) | 3.70 | 🟢 Normal | -0.052 |  |
| 2026-06-14 07:02:50 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.054 |  |
| 2026-06-14 06:27:46 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | -0.060 |  |
| 2026-06-14 06:02:34 | Peradeniya (Mahaweli Ganga) | 2.14 | 🟢 Normal | -0.082 |  |
| 2026-06-14 06:04:02 | Rathnapura (Kalu Ganga) | 3.96 | 🟢 Normal | -0.089 |  |
| 2026-06-14 07:03:01 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.090 |  |
| 2026-06-14 06:09:25 | Panadugama (Nilwala Ganga) | 4.05 | 🟢 Normal | -0.102 |  |
| 2026-06-14 07:01:23 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.121 |  |
| 2026-06-14 06:01:38 | Magura (Kalu Ganga) | 3.15 | 🟢 Normal | -0.160 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)