# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--14_05:01:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **205,670 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-14 05:01:26 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.014 |  |
| 2026-07-14 05:01:25 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-14 05:01:04 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -4.971 |  |
| 2026-07-14 05:00:55 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.011 |  |
| 2026-07-14 05:00:12 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-14 05:00:11 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-14 04:57:05 | Peradeniya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -4.971 |  |
| 2026-07-14 04:47:18 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-14 04:24:42 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.008 |  |
| 2026-07-14 04:22:03 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.049 |  |
| 2026-07-14 04:19:43 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-07-14 04:17:24 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | -0.014 |  |
| 2026-07-14 04:16:10 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-14 04:12:48 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-14 04:03:08 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-14 04:01:25 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-14 04:01:00 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-14 04:12:48 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-14 04:10:18 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-14 04:19:43 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-07-14 04:10:45 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-14 04:02:53 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-14 04:04:16 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-14 04:02:31 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-14 04:03:18 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-14 04:02:10 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:04:38 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-14 03:03:45 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-07-14 01:06:35 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-14 04:47:18 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-14 04:04:01 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-07-14 03:09:46 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:04:34 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-14 04:05:46 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | 0.000 |  |
| 2026-07-14 05:00:11 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-14 04:16:10 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-14 04:02:47 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:02:04 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-14 05:01:25 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-14 04:01:16 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-14 04:01:34 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-14 05:00:12 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-14 03:27:26 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.007 |  |
| 2026-07-14 04:24:42 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.008 |  |
| 2026-07-14 04:02:25 | Dunamale (Aththanagalu Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-07-14 05:00:55 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.011 |  |
| 2026-07-14 05:01:26 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.014 |  |
| 2026-07-14 04:22:03 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.049 |  |
| 2026-07-14 04:09:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.054 |  |
| 2026-07-14 04:07:41 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.064 |  |
| 2026-07-13 18:03:05 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.067 |  |
| 2026-07-14 04:08:13 | Hanwella (Kelani Ganga) | 0.94 | 🟢 Normal | -0.242 |  |
| 2026-07-14 05:01:04 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -4.971 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)