# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--28_05:03:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **299,956 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Putupaula — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 05:03:27 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | -0.071 |  |
| 2026-10-28 05:03:19 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-28 05:02:58 | Magura (Kalu Ganga) | 4.41 | 🟡 Alert | -0.019 |  |
| 2026-10-28 05:02:47 | Glencourse (Kelani Ganga) | 11.94 | 🟢 Normal | -0.020 |  |
| 2026-10-28 05:02:44 | Dunamale (Aththanagalu Oya) | 4.26 | 🟡 Alert | -0.060 |  |
| 2026-10-28 05:02:23 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-28 05:02:04 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | -0.033 |  |
| 2026-10-28 05:02:03 | Badalgama (Maha Oya) | 3.76 | 🟢 Normal | -0.025 |  |
| 2026-10-28 05:01:21 | Peradeniya (Mahaweli Ganga) | 3.02 | 🟢 Normal | 0.000 |  |
| 2026-10-28 05:01:11 | Moragaswewa (Deduru Oya) | 3.40 | 🟢 Normal | -0.123 |  |
| 2026-10-28 05:00:57 | Thalgahagoda (Nilwala Ganga) | 1.78 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-10-28 05:00:44 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-28 05:00:43 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-28 05:00:00 | Peradeniya (Mahaweli Ganga) | 3.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 04:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.86 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-10-28 05:00:57 | Thalgahagoda (Nilwala Ganga) | 1.78 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-10-28 04:06:17 | Baddegama (Gin Ganga) | 4.22 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-28 04:12:14 | Panadugama (Nilwala Ganga) | 6.01 | 🟠 Minor Flood | -0.009 |  |
| 2026-10-28 04:09:10 | Putupaula (Kalu Ganga) | 3.55 | 🟡 Alert | 0.037 | 🔺 Rising |
| 2026-10-28 03:11:38 | Ellagawa (Kalu Ganga) | 10.42 | 🟡 Alert | 0.000 |  |
| 2026-10-28 05:02:58 | Magura (Kalu Ganga) | 4.41 | 🟡 Alert | -0.019 |  |
| 2026-10-28 05:02:44 | Dunamale (Aththanagalu Oya) | 4.26 | 🟡 Alert | -0.060 |  |
| 2026-10-28 04:02:41 | Rathnapura (Kalu Ganga) | 6.92 | 🟡 Alert | -0.074 |  |
| 2026-10-28 04:01:11 | Moraketiya (Walawe Ganga) | 1.51 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-28 04:04:03 | Urawa (Nilwala Ganga) | 1.67 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-28 05:02:23 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-28 04:00:20 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-28 05:00:44 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-28 04:03:24 | Norwood (Kelani Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-28 04:03:22 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-28 05:03:19 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-28 04:09:10 | Thawalama (Gin Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-10-28 05:01:21 | Peradeniya (Mahaweli Ganga) | 3.02 | 🟢 Normal | 0.000 |  |
| 2026-10-28 04:06:44 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 18:23:14 | Galgamuwa (Mee Oya) | 4.03 | 🟢 Normal | -0.008 |  |
| 2026-10-28 04:09:29 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.009 |  |
| 2026-10-28 04:05:24 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-10-28 04:08:01 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-10-28 04:03:59 | Horowpothana (Yan Oya) | 3.37 | 🟢 Normal | -0.010 |  |
| 2026-10-28 04:02:17 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-10-28 03:03:38 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-10-28 05:02:47 | Glencourse (Kelani Ganga) | 11.94 | 🟢 Normal | -0.020 |  |
| 2026-10-28 04:03:26 | Hanwella (Kelani Ganga) | 4.78 | 🟢 Normal | -0.020 |  |
| 2026-10-28 04:08:13 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | -0.024 |  |
| 2026-10-28 05:02:03 | Badalgama (Maha Oya) | 3.76 | 🟢 Normal | -0.025 |  |
| 2026-10-28 05:02:04 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | -0.033 |  |
| 2026-10-27 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.059 |  |
| 2026-10-28 04:02:27 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.060 |  |
| 2026-10-28 05:03:27 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | -0.071 |  |
| 2026-10-28 04:04:42 | Kithulgala (Kelani Ganga) | 2.21 | 🟢 Normal | -0.085 |  |
| 2026-10-28 05:01:11 | Moragaswewa (Deduru Oya) | 3.40 | 🟢 Normal | -0.123 |  |
| 2026-10-27 18:00:41 | Thanthirimale (Malwathu Oya) | 2.72 | 🟢 Normal | -0.133 |  |
| 2026-10-28 04:00:24 | Pitabeddara (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.161 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)